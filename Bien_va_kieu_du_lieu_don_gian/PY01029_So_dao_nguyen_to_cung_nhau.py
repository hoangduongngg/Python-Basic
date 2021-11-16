import math
def So_dao(n):
    n = list(reversed(str(n)))
    res=""
    for i in n:
        res+=i
    return int(res)
    
def Check(n):
    if math.gcd(n, So_dao(n))==1:
        return 1
    return 0

t = int (input())
while t>0:
    n = int(input())
    if Check(n):
        print("YES")
    else:
        print("NO")
    t-=1