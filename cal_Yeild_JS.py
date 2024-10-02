import rasterio
import numpy as np

class ImageProcessor:
    def __init__(self, evi073_path, evi081_path, evi097_path, evi105_path):
        """
                 :param evi073_path :  EVI1
                 :param evi081_path:  EVI2
                 :param evi097_path:  EVI4
                 :param evi105_path:   EVI5

        """
        self.evi073 = self.read_image(evi073_path)
        self.evi081 = self.read_image(evi081_path)
        self.evi097 = self.read_image(evi097_path)
        self.evi105 = self.read_image(evi105_path)

    def read_image(self, path):
        with rasterio.open(path) as src:
            return src.read(1), src.profile

    def calculate_model1(self):
        model1 = 0.863 * self.evi073 - 0.851 * self.evi081 + 0.497 * self.evi097 + 0.916 * self.evi105 + 0.088
        return model1

    def calculate_model2(self):
        model2 = 0.293 * self.evi073 + 0.730 * self.evi097 + 0.191
        return model2

    def calculate_model3(self):
        model3 = 1.008 * self.evi073 + 0.683 * self.evi081 - 0.987 * self.evi105 + 0.449
        return model3

    def save_image(self, data, profile, output_path):
        profile.update(dtmodelpe=rasterio.float32, count=1)
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(data.astmodelpe(rasterio.float32), 1)

    def process_and_save_all(self, output_paths):
        model1 = self.calculate_model1()
        model2 = self.calculate_model2()
        model3 = self.calculate_model3()

        self.save_image(model1, self.evi073, output_paths['model1'])
        self.save_image(model2, self.evi073, output_paths['model2'])
        self.save_image(model3, self.evi073, output_paths['model3'])

        # Stack images together
        stacked = np.stack([model1, model2, model3], axis=0)
        self.save_image(stacked, self.evi073, output_paths['stacked'])

if __name__ == "__main__":
    evi_paths = {
        'evi073': 'EVI073.tif',#替换成4个EVI路径
        'evi081': 'EVI081.tif',
        'evi097': 'EVI097.tif',
        'evi105': 'EVI105.tif'
    }

    output_paths = {
        'model1': 'model1.tif',#替换成苏北，中，南估产地图保存路径
        'model2': 'model2.tif',
        'model3': 'model3.tif',
        'stacked': 'stacked.tif'#替换成江苏省估产地图保存路径
    }

    processor = ImageProcessor(evi_paths['evi073'], evi_paths['evi081'], evi_paths['evi097'], evi_paths['evi105'])
    processor.process_and_save_all(output_paths)
