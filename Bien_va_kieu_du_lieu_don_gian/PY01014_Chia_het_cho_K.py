def Run(a,K,N):
    res = []
    if a>=N or K>N:
        res.append(-1)
        return res

    x, y = a//K, N//K
    for i in range(x+1,y+1):
        res.append(i*K-a)
    if len(res)==0:
        res.append(-1)
    return res

data = input().split()
a, K, N = int(data[0]), int (data[1]), int (data[2])
for i in Run(a,K,N):
    print(i, end = " ")