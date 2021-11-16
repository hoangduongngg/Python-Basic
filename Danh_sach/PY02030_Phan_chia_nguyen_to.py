import math
def Phan_chia(a):
    a_set = list(set(a))
    b = []
    for i in a:
        if i in a_set:
            b.append(i)
            a_set.remove(i)
    temp = 0
    for i in b:
        temp +=i
        if SNT(temp) and SNT(sum(b)-temp):
            return b.index(i)
    return -1

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
if Phan_chia(a)>=0:
    print(Phan_chia(a))
else:
    print("NOT FOUND")