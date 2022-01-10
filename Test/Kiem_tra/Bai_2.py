import math
def SNT(n):
    if n==2:
        return 1
    if n%2 ==0 or n<2:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1

def SNT_thu_n (n):
    a = [2]
    i = 3
    while len(a)<n:
        if SNT(i):
            a.append(i)
        i+=2
    return a[n-1]

n = 30 + 3
print(SNT_thu_n(n))