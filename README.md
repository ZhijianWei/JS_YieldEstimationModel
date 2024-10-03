# <div align="center">Remote Sensing Crop Yield Estimation for Jiangsu Province
## <div align="center"><b><a href="README.md">English</a> | <a href=READMEzh.md>简体中文</a></b></div>

#### Author: Zhijian Wei (Nanjing Agricultural University). If you have any questions, please feel free to contact me at ``18151936092@163.com``📧
**If this algorithm is helpful to you, please give this project a Star ⭐, or recommend it to your friends. Thank you! 😊**

## 💻Project Overview
!032fef67686420e2d71c827d7414b80
!cfdbba722570b7ac2b8c84e090e2afb
!ea9961cf2e681cd2c2b93807caf69cb
### <div align="center"> Spatial Distribution of Wheat Yield Estimation Sample Points in Jiangsu Province <br><br>
  
## ⚡Code Description (Model based on 2023 EVI, for demonstration purposes only):<br><br>
### 1. Import sampling points and study area shapefile into Google Earth Engine, use modisEVI(GEE).txt to download preprocessed time series EVI images for the corresponding year (set the date from the first year's sowing to the second year's sowing).
### 2. Explore regression relationships based on different EVI and measured yield data (JSyield_summary(averaged).csv), construct yield estimation models for three regions, and repeatedly calibrate to determine the best coefficients using accuracy indicators.
<br><br>
!e58591163576d21b00caf83157783e2
!137da06c0bf570b41a8cfc72528f85c
!c76764b1eb48b93734af36733cfb517

### 3. Use cal_Yield_JS.py to calculate yield and stitch images.
### 4. Use software like ArcGIS to mask and map wheat yield using the wheat production area as the base map.<br><br>
## 👀Results (Partial):
!fc5604bb394def82e75d52e69741c1e
### <div align="center"> Spatial Distribution of Wheat Yield in Jiangsu Province
!032fef67686420e2d71c827d7414b80
### <div align="center"> Detailed Map of Wheat Yield Distribution in Jiangsu Province
!f95ef93afb92bd49328566ec9ee7b50
### <div align="center"> Spatial Distribution of Wheat Yield in Xuzhou City
!a8aa9f6d0b4ca3528a9879b7932eed0
### <div align="center"> Spatial Distribution of Wheat Yield in Lianyungang City

