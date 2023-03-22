"""
Lab03 - zadanie 04
"""

limit = int(input("Podaj liczbę graniczną: "))

catalanNumber = 1
print(catalanNumber)
for n in range(0, limit + 1):
    catalanNumber *= 2 * (2 * n + 1) / (n + 2)
    if catalanNumber > limit:
        break
    print(int(catalanNumber))
