"""
Lab03 - zadanie 05
"""

db = []
choice = -1
while choice != 0:
    choice = int(input("Podaj wybór: "))
    if choice == 1:
        number = int(input("Podaj liczbę do dodania: "))
        db.append(number)
    if choice == 2:
        number = int(input("Podaj liczbę do usunięcia: "))
        db.remove(number)
    if choice == 3:
        numbers = [int(x) for x in input("Podaj liczby do zamiany: ").split(",")]

        db.remove(number)