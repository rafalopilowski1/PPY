"""
Lab03 - zadanie 02
"""


numbers = [int(x) for x in input("Podaj po przecinku 20 liczb z zakresu od -20 do 20: ").split(",")]
numberCopy = [int(x) for x in numbers]

notPrime = []
for x in numberCopy:
    for i in range(2, x):
        if x % i == 0:
            notPrime.append(x)
            break

primeTuple = tuple(x for x in numberCopy if x not in notPrime)
twoTuple = tuple(2 ** x for x in numbers if x % 2 == 0)
replaced = list(map(lambda x: str(x) if x % 2 != 0 else "A", numberCopy))

print(numbers)
print(numberCopy)
print(primeTuple)
print(twoTuple)
print(replaced)
