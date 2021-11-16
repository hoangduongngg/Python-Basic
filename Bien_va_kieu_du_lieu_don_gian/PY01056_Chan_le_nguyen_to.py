import math
def Check(n):
    sum=0
    for i in range(0, len(n)):
        sum+= int(n[i])
        if (i%2==0 and int (n[i])%2!=0) or (i%2!=0 and int (n[i])%2==0):
            return 0

    if SNT(sum):
        return 1
    return 0

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
    n = input()
    if Check(n):
        print("YES")
    else:
        print("NO")
    t-=1