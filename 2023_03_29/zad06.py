"""
Lab04 - zadanie 6
"""

x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))

print(sum([x for x in range(x, y + 1) if x % 2 != 0]))
