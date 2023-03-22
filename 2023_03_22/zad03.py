"""
Lab03 - zadanie 03
"""

count = int(input("Podaj rząd tabliczki mnożenia: "))

for i in range(1, count+1):
    for j in range(1, count+1):
        print(i*j, end=' ')
    print()
