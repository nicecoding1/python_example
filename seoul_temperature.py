import pandas as pd

f_name = "seoul_temperature.csv"
df = pd.read_csv(f_name, header=0, index_col=0, encoding='utf-8')
df.columns=['Location', 'Temp_avg', 'Temp_low', 'Temp_high']
df.index.name = "Date"

print(df.head())
print()

t1 = df['Temp_avg'].mean()
print("기상 관측 이래 서울의 평균기온의 평균값 : %.2f" % t1)

t2 = df['Temp_low'].min()
print("기상 관측 이래 서울의 최저기온의 최소값 : %.2f" % t2)

t3 = df['Temp_high'].max()
print("기상 관측 이래 서울의 최고기온의 최대값 : %.2f" % t3)
