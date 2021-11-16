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

def Liet_ke(a,n):
    b = list(set(a))

    for i in a:
        if SNT(i)==1 and b.count(i)==1:
            print(f"{i} {a.count(i)}")
            b.remove(i)

n = int (input())
a = [int(i) for i in input().split()]
Liet_ke(a,n)