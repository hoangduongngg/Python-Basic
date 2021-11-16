import math
def Check(n):
    if len(n)<4:
        return 0
    if SNT( int(n[0:3]) ) and SNT ( int(n[-3:len(n)]) ):
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