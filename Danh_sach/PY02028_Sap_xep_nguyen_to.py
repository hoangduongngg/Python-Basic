import math
def Sort_NT(a):
    b = []
    res = []
    for i in a:
        if SNT(i):
            b.append(i)
    b = sorted(b)
    j=0
    for i in a:
        if SNT(i):
            res.append(b[j])
            j+=1
        else:
            res.append(i)
    return res

def SNT(n):
    if n==2:
        return 1
    if n%2 ==0 or n<2:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1
n = int (input())
a = [int(i) for i in input().split()]
print(*Sort_NT(a))