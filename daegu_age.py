import pandas as pd
from matplotlib import pyplot as plt

colm = "0~9세,10~19세,20~29세,30~39세,40~49세,50~59세,60~69세,70~79세,80~89세,90~99세,100세 이상".split(',')
df = pd.read_csv("daegu_age.csv", encoding="euc-kr")
is_dong = df['행정구역'] == '대구광역시 중구 동인동(2711051700)'
df2 = df[is_dong]
data = df2[colm].values.tolist()[0]
data2 = []

for i in data:
    data2.append(int(str(i).replace(',', '')))

plt.rcParams["font.family"] = 'NanumGothic'
plt.figure(figsize=(12, 6))
plt.plot(colm, data2)
plt.show()