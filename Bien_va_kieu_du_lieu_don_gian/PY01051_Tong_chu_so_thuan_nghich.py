import math
def Check(n):
    sum=int(n[0])
    for i in range(1, len(n)):
        sum+= int(n[i])
    if STN(sum):
        return 1
    return 0

def STN(n): #so thuan nghich
    n = str(n)
    if len(n)==1:
        return 0
    for i in range(0, int (len(n)/2)):
        if n[i]!=n[-1-i]:
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