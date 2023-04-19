"""
Test data
 - (2)(5)(4)(3)(6)(5)(4)(3)(6)(8)(4)(3)(2)(1)(2)(6)(5)(2)(1)(8)
 - (5)(1)(6)(2)(7)(5)(4)(8)(5)(3)(6)(3)(8)(1)(8)(5)(2)(1)(8)(6)
"""

print("Podaj liczbę ramek: ", end="")
capacity = int(input())
f, st, fault, pf = [], [], 0, 'No'
print("Podaj ramki: ", end="")
s = list(map(int, input().strip().replace('(', '').replace(')', ' ').split()))
print("\nTime|Frame →\t", end='')
for i in range(capacity):
    print(i + 1, end=' ')
print("Fault\n   ↓\n")
for index, i in enumerate(s):
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f) - 1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Yes'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'No'
    print(f"   {index + 1}\t\t", end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print(f"\nTotal Requests: {len(s)}\nTotal Page Faults: {fault}\nFault Rate: {(fault / len(s)) * 100}%")
