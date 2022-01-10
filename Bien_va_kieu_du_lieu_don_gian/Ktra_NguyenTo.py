def SNT(n):
    if n==2: return 1
    if n<2 or n%2==0: return 0
    i=3
    while i*i<=n:
        if n%i==0: return 0
        i+=2
    return 1

def Ktra_NguyenTo (n):
    n = n[-4:len(n)]
    if SNT(int(n)): return 1
    return 0

def Check(n):
    if Ktra_NguyenTo(n): print("YES")
    else: print("NO")
    
t = int(input())
while t>0:
    Check(input())
    t-=1