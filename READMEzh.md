# <div align="center">江苏省小麦产量遥感估算
## <div align="center"><b><a href="https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/README.md">English</a> | <a href="https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/READMEzh.md">简体中文</a></b></div>

#### 作者：魏智健 (南京农业大学) ，如果有任何问题，请随时联系我``18151936092@163.com``📧
**如果这套算法对你有帮助，可以给本项目一个 Star ⭐ ，或者推荐给你的朋友们，谢谢！😊**

## 💻项目简介
![032fef67686420e2d71c827d7414b80](https://github.com/user-attachments/assets/6be1c2e6-32ec-4271-a744-4dd26f62adfa)
![cfdbba722570b7ac2b8c84e090e2afb](https://github.com/user-attachments/assets/c8d7c181-58ab-422f-8afb-54f6349f7c5d)
![ea9961cf2e681cd2c2b93807caf69cb](https://github.com/user-attachments/assets/0d27415d-c994-40e8-aa76-19ed5eb2cbd1)
### <div align="center"> 江苏省小麦估产样点空间分布 <br><br>
  
## ⚡代码说明(模型基于2023年EVI制作,仅作示例):<br><br>
### 1.在GoogleEarthEngine中导入采样点和研究区shp,使用 modisEVI(GEE).txt 下载预处理后对应年份的时间序列EVI影像(日期设置为第一年播种到第二年播种)
![image](https://github.com/ZhijianWei/RS-YieldEstimationModel-for-JS/blob/main/output_map/EVI_down.png)
### 2.根据不同的EVI和产量实测数据( JSyield_summary(averaged).csv )挖掘回归关系,构建三个地区的估产模型,并通过精度指标反复校正确定最佳系数
<br><br>
![e58591163576d21b00caf83157783e2](https://github.com/user-attachments/assets/1c2d3344-c684-4bec-a0da-2b98857007d8)
![137da06c0bf570b41a8cfc72528f85c](https://github.com/user-attachments/assets/1c18d9da-0b79-4980-b2d7-74bb1d67a1b5)
![c76764b1eb48b93734af36733cfb517](https://github.com/user-attachments/assets/a92563b5-4888-4e96-8f29-69751510f2ab)

### 3.使用 cal_Yield_JS.py 来计算产量和拼接图像
### 4.使用ArcGIS等软件用小麦产区作底图对小麦产量进行掩膜并出图<br><br>
## 👀结果展示(部分):
![fc5604bb394def82e75d52e69741c1e](https://github.com/user-attachments/assets/671e42f6-e7b8-4918-91fd-9e7acfff8d1e)
### <div align="center"> 江苏省小麦单产空间分布
![032fef67686420e2d71c827d7414b80](https://github.com/user-attachments/assets/e88b59b0-8f5a-4dc4-906b-c558d057e152)
### <div align="center"> 江苏省小麦单产空间分布细节图
![f95ef93afb92bd49328566ec9ee7b50](https://github.com/user-attachments/assets/a9f13372-4889-4f83-af5b-73f2e42edbd9)
### <div align="center"> 徐州市小麦单产空间分布
![a8aa9f6d0b4ca3528a9879b7932eed0](https://github.com/user-attachments/assets/5d8ca818-d2f4-4fd0-9911-6417e6fd806a)
### <div align="center"> 连云港市小麦单产空间分布<br><br>

## 🤗特别感谢
[@YueyueZang](https://github.com/YueyueZang)对回归关系的挖掘和估产模型的校正


