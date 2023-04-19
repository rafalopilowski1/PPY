"""
Test data
 - (2)(5)(4)(3)(6)(5)(4)(3)(6)(8)(4)(3)(2)(1)(2)(6)(5)(2)(1)(8)
 - (5)(1)(6)(2)(7)(5)(4)(8)(5)(3)(6)(3)(8)(1)(8)(5)(2)(1)(8)(6)
"""

print("Podaj liczbę ramek: ", end="")
capacity = int(input())
f, fault, pf = [], 0, 'No'
print("Podaj ramki: ", end="")
s = list(map(int, input().strip().replace('(', '').replace(')', ' ').split()))
print("\nTime|Frame →\t", end='')
for i in range(capacity):
    print(i + 1, end=' ')
print("Fault\n   ↓\n")
occurance = [None for i in range(capacity)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f) < capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i + 1:]:
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i + 1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print(f"   {i + 1}\t\t", end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"\nTotal Requests: {len(s)}\nTotal Page Faults: {fault}\nFault Rate: {(fault / len(s)) * 100}%")
