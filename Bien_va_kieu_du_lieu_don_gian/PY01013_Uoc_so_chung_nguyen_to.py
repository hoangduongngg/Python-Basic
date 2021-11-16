import math
def Check(a,b):
    if SNT(Tong_cs (math.gcd(a,b)))==1:
        return 1
    return 0

def Tong_cs(n):
    res=0
    n = str(n)
    for i in n:
        res += int(i)
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

t = int (input())
while t>0:
    data = input().split(" ")
    a, b = int (data[0]), int (data[1])
    if Check(a,b):
        print("YES")
    else:
        print("NO")

    t-=1