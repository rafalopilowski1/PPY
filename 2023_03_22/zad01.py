"""
Lab03 - zadanie 1
"""

name = input("Podaj imię: ")
birthDate = input("Podaj datę urodzenia (w formacie ISO): ")
emailAddress = input("Podaj adres e-mail: ")
phoneNumber = input("Podaj number telefonu: ")

inputList = [name, birthDate, emailAddress, phoneNumber]
inputTuple = (name, birthDate, emailAddress, phoneNumber)
inputDict = {name, birthDate, emailAddress, phoneNumber}

print(inputList)
print(inputTuple)
print(inputDict)
