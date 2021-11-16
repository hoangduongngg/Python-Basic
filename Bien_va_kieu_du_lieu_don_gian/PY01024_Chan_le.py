import math
def Check(n):
    sum=int(n[0])
    for i in range(1, len(n)):
        sum+= int(n[i])
        if abs( int(n[i]) - int(n[i-1]) )!=2:
            return 0
    if sum%10!=0:
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