def Run(a,K,N):
    res = []
    if a>=N or K>N:
        return res.append(-1)

    x, y = a//K, N//K
    for i in range(x+1,y+1):
        res.append(i*K-a)
        
    if len(res)==0:
        res.append(-1)
    return res

a, K, N = map(int, input().split())
print(*Run(a,K,N))

# input
# 10 6 40
# Out 
# 2 8 14 20 26