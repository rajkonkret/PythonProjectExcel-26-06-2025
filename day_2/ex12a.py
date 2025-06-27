import pandas
import pandas as pd

data = [
    ["Adiya", 179],
    ["Samen", 181],
    ["Darek", 170],
    ["John", 167],
]

column_names = ['Name', 'Height']

df = pd.DataFrame(data, columns=column_names)
writer = pd.ExcelWriter('excel_with_list.xlsx', engine='xlsxwriter')

# df.to_excel(writer, sheet_name='first_sheet', index=False, startrow=3, startcol=4)
# df.to_excel(writer, sheet_name='first_sheet', index=True, startrow=3, startcol=4)
df.to_excel(writer, sheet_name='first_sheet', index=True, startrow=3)
writer.close()
