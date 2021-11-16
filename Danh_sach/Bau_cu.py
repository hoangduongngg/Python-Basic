def Bau_cu(a,n,m):
    b = []
    for i in range(1,m+1):
        b.append([i, a.count(i)])
    b = sorted(b, key = lambda k:[k[1], -k[0]], reverse=True)
    for i in range(0,m):
        if b[i][1]<b[0][1]:
            return b[i][0]
    return -1

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
if Bau_cu(a,n,m)==-1:
    print("NONE")
else:
    print(Bau_cu(a,n,m))