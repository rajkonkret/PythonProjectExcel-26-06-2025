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

"""Komentarz
 wielolinijkowy"""

print('''Tekst
wielolinijkowy''')
# Tekst
# wielolinijkowy

print(100 / 2)  # dzielenie
print(100 // 2)  # czesc całkowita dzielenia
print(100 % 3)  # modulo, reszta z dzielenia

zysk = 890987654321
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 890,987,654,321
print(f"Nasza duża liczba: {zysk:_}")  # Nasza duża liczba: 890_987_654_321
print(f"Nasza duża liczba: {zysk:_}".replace("_", " "))  # Nasza duża liczba: 890 987 654 321

zysk = 890_987_654_321
print(type(zysk))
print(zysk)  # 890987654321

encoded_text = tekst.encode('utf-8')
print(encoded_text)  # b'witaj \xc5\x9awiecie'
print(type(encoded_text))  # <class 'bytes'>
print(encoded_text.decode('utf-8'))  # witaj Świecie

# kolekcje
# lista, krotka(tuple), zbiór(set), słownik

lista = [5, 6, 7, 8, 9, "Radek"]
print(lista)  # [5, 6, 7, 8, 9, 'Radek']

lista2 = lista  # kopia referencji
print(lista)  # [5, 6, 7, 8, 9, 'Radek']
print(lista2)  # [5, 6, 7, 8, 9, 'Radek']

lista_copy = lista.copy()
lista.clear()  # czysci elementy listy
print(lista)
print(lista2)
print(lista_copy)  # [5, 6, 7, 8, 9, 'Radek']
print(lista_copy)

# krotka - tuple
krotka = tuple(lista_copy)
print(krotka)  # lista do odczytu, pozwala efektywniej zarzadzac pamięcia

zbior = {5, 6, 5, 6, 6, 7, 8, 9, 0}  # przechowuje unikalne wartosc
print(zbior)
# nie zachowuje kolejności przy dodawaniu elementów
zbior_lista = set(lista_copy)
print(zbior_lista)  # {5, 6, 7, 8, 9, 'Radek'}

slownik = {'name': "radek", 'age': 45}
print(slownik)  # {'name': 'radek', 'age': 45}
print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'age'])
# dict_values(['radek', 45])
# dict_items([('name', 'radek'), ('age', 45)])
slownik2 = {"name": ["Radek", "Tomek", "Piotr"]}
print(slownik2)  # {'name': ['Radek', 'Tomek', 'Piotr']}
