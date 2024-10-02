## 1.项目简介
![032fef67686420e2d71c827d7414b80](https://github.com/user-attachments/assets/6be1c2e6-32ec-4271-a744-4dd26f62adfa)
![cfdbba722570b7ac2b8c84e090e2afb](https://github.com/user-attachments/assets/c8d7c181-58ab-422f-8afb-54f6349f7c5d)
![ea9961cf2e681cd2c2b93807caf69cb](https://github.com/user-attachments/assets/0d27415d-c994-40e8-aa76-19ed5eb2cbd1)
### <div align="center"> 江苏省小麦估产样点空间分布 <br><br>
  
## 2.代码说明(模型基于2023年EVI制作,仅作示例):<br><br>
### *在GoogleEarthEngine中导入采样点和研究区shp,使用 modisEVI(GEE).txt 下载预处理后对应年份的时间序列EVI影像(日期设置为第一年播种到第二年播种)
### *根据不同的EVI和产量实测数据挖掘回归关系,构建三个地区的估产模型,并通过精度指标反复校正确定最佳系数
### *使用 cal_Yield_JS.py 来计算产量和拼接图像
### *使用ArcGIS等软件用小麦产区作底图对小麦产量进行掩膜并出图
## 3.结果展示(部分):
![fc5604bb394def82e75d52e69741c1e](https://github.com/user-attachments/assets/671e42f6-e7b8-4918-91fd-9e7acfff8d1e)
### <div align="center"> 江苏省小麦单产空间分布
![032fef67686420e2d71c827d7414b80](https://github.com/user-attachments/assets/e88b59b0-8f5a-4dc4-906b-c558d057e152)
### <div align="center"> 江苏省小麦单产空间分布细节图
![f95ef93afb92bd49328566ec9ee7b50](https://github.com/user-attachments/assets/a9f13372-4889-4f83-af5b-73f2e42edbd9)
### <div align="center"> 徐州市小麦单产空间分布
![a8aa9f6d0b4ca3528a9879b7932eed0](https://github.com/user-attachments/assets/5d8ca818-d2f4-4fd0-9911-6417e6fd806a)
### <div align="center"> 连云港市小麦单产空间分布


