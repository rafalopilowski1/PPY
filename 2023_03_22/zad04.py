"""
Lab03 - zadanie 04
"""

limit = int(input("Podaj liczbę graniczną: "))
catalanNumber = 1
print(catalanNumber)
n = 0
while catalanNumber <= limit:
    catalanNumber *= 2 * (2 * n + 1) // (n + 2)
    print(catalanNumber)
    n += 1
