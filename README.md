# <div align="center">Remote Sensing Crop Yield Estimation for Jiangsu Province
## <div align="center"><b><a href="https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/README.md">English</a> | <a href="https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/READMEzh.md">简体中文</a></b></div>

#### Author: Zhijian Wei (Nanjing Agricultural University). If you have any questions, please feel free to contact me at ``18151936092@163.com``📧
**If this algorithm is helpful to you, please give this project a Star ⭐, or recommend it to your friends. Thank you! 😊**

## 💻Introduction
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/detailed_output.png)
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/roadmap.jpg)
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/SP_distribution.png)
### <div align="center"> Spatial Distribution of Wheat Yield Estimation Sample Points in Jiangsu Province <br><br><br><br>
  
## ⚡Instructions (Model based on 2023 EVI, for demonstration purposes only):<br><br>
### 1. Import sampling points and study area shapefile into Google Earth Engine, use modisEVI(GEE).txt to download preprocessed time series EVI images for the corresponding year (set the date from the first year's sowing to the second year's sowing).
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/EVI_down.png)
### 2. Explore regression relationships based on different EVI and measured yield data (JSyield_summary(averaged).csv), construct yield estimation models for three regions, and repeatedly calibrate to determine the best coefficients using accuracy indicators.
<br><br>
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/model1.jpg)
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/model2.jpg)
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/model3.jpg)
### 3. Use cal_Yield_JS.py to calculate yield and stitch images.
### 4. Use software like ArcGIS to mask and map wheat yield using the wheat production area as the base map.<br><br><br><br>
## 👀Results (Partial):
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/JS_output.png)
### <div align="center"> Spatial Distribution of Wheat Yield in Jiangsu Province
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/detailed_output.png)
### <div align="center"> Detailed Map of Wheat Yield Distribution in Jiangsu Province
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/Xuzhou_output.png)
### <div align="center"> Spatial Distribution of Wheat Yield in Xuzhou City
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/Lianyungang_output.png)
### <div align="center"> Spatial Distribution of Wheat Yield in Lianyungang City<br><br><br><br>

