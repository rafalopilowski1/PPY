"""
Lab03 - zadanie 05
"""

db = dict()
choice = -1
while choice != 0:
    choice = int(input("Podaj wybór: "))
    if choice == 0:
        print("Do zobaczenia!")
    if choice == 1:  # Dodawanie
        name = input("Podaj nazwę produktu: ")
        amount = int(input("Podaj ilość: "))
        price = float(input("Podaj cenę: "))
        item = (name, amount, price)
        id = len(db) + 1
        db[id] = item
        print(f"Dodano produkt: {id}: {item}")
        print("Gotowe!")
    if choice == 2:  # Usuwanie
        number = int(input("Podaj numer produktu do usunięcia: "))
        db.pop(number)
        print("Gotowe!")
    if choice == 3:  # Modyfikacja
        number = int(input("Podaj numer produktu do modyfikacji: "))
        (name, amount, price) = db[number]
        db.pop(number)
        newName = input(f"Nazwa: {name} --> ")
        newAmount = int(input(f"Ilość: {amount} --> "))
        newPrice = float(input(f"Cena: {price} --> "))
        db[number] = (newName, newAmount, newPrice)
        print("Gotowe!")
    if choice == 4:
        number = int(input("Podaj liczbę do wyświetlenia: "))
        print(db[number])
        print("Gotowe!")
