import pandas as pd

df = pd.read_excel("../data/excel_without_index-1.xlsx")

print("The dataframe is:")
print(df)
# The dataframe is:
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df = pd.read_excel("../data/excel_with_multiple_sheets-1.xlsx", sheet_name=2)

print("The dataframe is:")
print(df)
# The dataframe is:
#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67


df = pd.read_excel("../data/excel_with_multiple_sheets-1.xlsx", sheet_name="marks")

print("The dataframe is:")
print(df)
# The dataframe is:
#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67

data = pd.ExcelFile("../data/excel_with_multiple_sheets-1.xlsx")
print(data.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel("../data/excel_with_multiple_sheets-1.xlsx", sheet_name=data.sheet_names[0])

print("The dataframe is:")
print(df)
# The dataframe is:
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167

df = pd.read_excel("../data/excel_with_multiple_sheets-1.xlsx", sheet_name="marks", usecols=["Name"])

print("The dataframe is:")
print(df)
# The dataframe is:
#        Name
# 0    Aditya
# 1    Sameer
# 2  Dharwish
# 3      Joel
