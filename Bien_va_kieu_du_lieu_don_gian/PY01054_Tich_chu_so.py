def Tich_cs(n):
    res = 1
    for i in n:
        if i!='0':
            res*=int(i)
    return res

t = int(input())
while t>0:
    n = input()
    print(Tich_cs(n))
    t-=1