"""
Lab02 - Operacje na łańcuchach; Konwersja typów
"""

# napis = "Wiek " + 10
# print(napis)
"""
TypeError: can only concatenate str (not "int") to str
"""
napis = "Wiek " + str(10)  # Potrzebna konwersja
print(napis)  # OK

# Zamiana znaku w tekście

print(napis.replace('W', 'w'))

print(napis.upper())
print(napis.lower())

# Konwersja typu tekstowego na typ liczbowy

a = '5'
b = 7

print(int(a) + b)

# Konwersja typu liczbowego na typ tekstowy

a = '6'
b = 6

print(a + repr(b))  # pełna reprezentacja
print(a + str(b))  # skrócona (!!!)
