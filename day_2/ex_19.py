import pandas as pd

df = pd.read_excel("../data/excel_without_index-1.xlsx")
print(df)

print(df[df['Height'] > 175])
#      Name  Height
# 0  Aditya     179
# 1  Sameer     181

suma = df['Height'].sum(skipna=False)  # skipna - mon brakujące
print("Suma:", suma)  # Suma: 697

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    4 non-null      object
#  1   Height  4 non-null      int64

print(df.describe())
# <bound method NDFrame.describe of        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167>

print(df['Height'].describe())
# count      4.000000
# mean     174.250000
# std        6.800735
# min      167.000000
# 25%      169.250000
# 50%      174.500000
# 75%      179.500000
# max      181.000000
# Name: Height, dtype: float64

print(df["Height"].mean())  # 174.25
print(df["Height"].median())  # 174.5
