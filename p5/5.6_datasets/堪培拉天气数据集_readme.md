---
Ext:
    - .csv

DatasetUsage:
    - 15797678

FolderName:
    - /home/mw/input/canberraWeather2321/
---

## **背景描述**
该数据集包含堪培拉的历史天气数据集，其目的在于通过记录每日的天气数据预测第二天是否会下雨。

## **数据说明**
 - Date：观察特征的那一天
 - Location：观察的城市
 - MinTemp：当天最低温度（摄氏度）
 - MaxTemp：当天最高温度（摄氏度）温度都是 string
 - Rainfall：当天的降雨量（单位是毫米mm）
 - Evaporation：一个凹地上面水的蒸发量（单位是毫米mm），24小时内到早上9点
 - Sunshine：一天中出太阳的小时数
 - WindGustDir：最强劲的那股风的风向，24小时内到午夜
 - WindGustSpeed：最强劲的那股风的风速（km/h），24小时内到午夜
 - WindDir9am：上午9点的风向
 - WindDir3pm：下午3点的风向
 - WindSpeed9am：上午9点之前的十分钟里的平均风速，即 8:50~9:00的平均风速，单位是（km/hr）
 - WindSpeed3pm：下午3点之前的十分钟里的平均风速，即 14:50~15:00的平均风速，单位是（km/hr）
 - Humidity9am：上午9点的湿度
 - Humidity3pm：下午3点的湿度
 - Pressure9am：上午9点的大气压强（hpa）
 - Pressure3pm：下午3点的大气压强
 - Cloud9am：上午9点天空中云的密度，取值是[0, 8]，以1位一个单位，0的话表示天空中几乎没云，8的话表示天空中几乎被云覆盖了
 - Cloud3pm：下午3点天空中云的密度
 - Temp9am：上午9点的温度（单位是摄氏度）
 - Temp3pm：下午3点的温度（单位是摄氏度）
 - RainTomorrow：明天是否下雨标签

## **文件说明**
 - `train_weather.csv` 训练数据
 - `test_weather.csv` 测试数据
 - `submit_result.csv` 测试提交结果