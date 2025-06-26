#  PEP8
# ctrl alt l - formatuje kod wg PEP8
import sys

print()
print("Radek")
print('Radek')
# ctrl - d kopiowanie lini
# print('Radek") ctrl / - komentarz linijki
# C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025\.venv\Scripts\python.exe C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025\day_1\pierwszy.py
#   File "C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025\day_1\pierwszy.py", line 7
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
#
# Process finished with exit code 1
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>

print("39" + "14")  # konkatenacja 3914
print(39 + 14)  # 53

# print("39" + 14) # TypeError: can only concatenate str (not "int") to str
# silne typowanie
print(type(39))  # <class 'int'> - liczby calkowite
print(sys.int_info)
# 3 sys.int_info(bits_per_digit=30, sizeof_digit=4,
#                default_max_str_digits=4300, str_digits_check_threshold=640)

# zmienna - pudelko na dane
# przechowuje jeden element

name = "radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

age = 89
print(age)
# tylko podpowiedzi typu
name: str = 90

print(name) # 90
# mypy
# pip install mypy

# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025> mypy .\day_1\pierwszy.py
# day_1\pierwszy.py:37: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# day_1\pierwszy.py:44: error: Name "name" already defined on line 33  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025>
