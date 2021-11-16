import math
n = int (input())
a = (input().split(" "))
for i in range(0,n):
    a[i] = int(a[i])
a = sorted(a)
for i in range(0, n-1):
    for j in range(i+1, n):
        if math.gcd(a[i], a[j])==1:
            print(f"{a[i]} {a[j]}")