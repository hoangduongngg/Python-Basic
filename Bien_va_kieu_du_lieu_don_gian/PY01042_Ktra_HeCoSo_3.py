def Ktra_HeCoSo3 (n):
    a = set(list(n))
    if len(a) >3: return 0
    for i in a:
        if int(i)>2: return 0
    return 1

def Check(n):
    if Ktra_HeCoSo3(n): print("YES")
    else: print("NO")
    
t = int(input())
while t>0:
    Check(input())
    t-=1