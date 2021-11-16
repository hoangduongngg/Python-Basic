def Sort_Tich_cs (a,n):
    a = sorted(a, key = lambda k :(Tich_cs(k), int(k)) )
    for i in a:
        print(i , end = " ")
    print()

def Tich_cs (n):    #n:str
    res = 1
    for i in n:
        res*= int(i)
    return res

t = int (input())
while t>0:
    n = int (input())
    a = input().split()
    Sort_Tich_cs(a,n)
    t-=1