def Run(a,n):
    return Dem_cap(a) + Dem_cap(ChuyenVi(a,n))

def ChuyenVi(a,n):
    res = []
    for i in range(0,n):
        res.append([])
        for j in range(0,n):
            res[i].append(a[j][i])
    return res
    
def Dem_cap(a):
    res = 0
    for i in a:
        res += C_2_n(i.count('C'))
    return res

def C_2_n(x):
    return x*(x-1)//2

n = int(input())
a = []
for i in range(0,n):
    a.append(list(input()))
print(Run(a,n))