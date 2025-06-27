import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Próba {i}" for i in range(1, 6)])

print(df)
print(df.head())  # piec pierwszych
print(df.tail())  # pięc ostatnich
#      Próba 1   Próba 2   Próba 3   Próba 4   Próba 5
# 95 -1.310812 -0.815009 -1.106814  0.493950 -0.287733
# 96 -0.527926  0.101696  0.194969  1.256879  0.883062
# 97 -0.992483  0.585988  0.455140 -1.219787 -1.590231
# 98 -1.068604 -0.311818 -0.543749 -1.442129 -1.798535
# 99 -0.978056  0.482413  1.026700 -2.414493  0.718040

# xw.view(df)

book = xw.Book()
print(book.name)
print(book.sheets)

# Zeszyt1
# Sheets([<Sheet [Zeszyt1]Arkusz1>])

sheet1 = book.sheets[0]
sheet1 = book.sheets['Arkusz1']
print(sheet1.range("A1"))

sheet1.range("A1").value = [[1, 2],
                            [3, 4]]

sheet1.range("A4").value = 'Witaj!'

print(sheet1['A1'])  # <Range [Zeszyt1]Arkusz1!$A$1>

print(sheet1['A1'].value)  # 1.0

print(sheet1["A1:B2"])
print(sheet1["A1:B2"].value)  # [[1.0, 2.0], [3.0, 4.0]]
