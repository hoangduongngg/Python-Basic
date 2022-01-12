import math
def ChuyenVi (a):
    n = len(a)
    for i in range(0,n):
        for j in range(i,n):
            tmp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] =tmp
    return a

def DemCap (a):
    n = len(a)
    res = 0
    for i in a:
        res += math.comb(i.count('C'), 2)
    for i in ChuyenVi(a):
        res += math.comb(i.count('C'), 2)
    return res

n = int(input())
a = []
for i in range(0,n):
    a.append(list(input()))
print(DemCap(a))

# Input

# 4
# CC..
# C..C
# .CC.
# .CC.

# Output

# 9