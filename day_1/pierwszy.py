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

print(name)  # 90
# mypy
# pip install mypy

# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025> mypy .\day_1\pierwszy.py
# day_1\pierwszy.py:37: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# day_1\pierwszy.py:44: error: Name "name" already defined on line 33  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\cscomarch\PycharmProjects\PythonProjectExcel-26-06-2025>

tekst = "witaj Świecie"

print(tekst)
print(type(tekst))  # <class 'str'>

# teksty sa niemutowalne
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
zmienna = tekst.upper()
print(zmienna)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groß"
print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True

print(1 != 0)  # rózne

# rzutowanie
print(int("39"))
print(str(39))
print("14" + str(39))  # 1439

temp = 36.6
print(type(temp))  # zmiennoprzecinkowy

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004
# 12.345 + 1.0001 = 13.3451

# f - string format
print(f"Nazywam się {name}")
print("Nazywam się {}".format(name))

print("Nazywam się %s" % name)  # Nazywam się 90
