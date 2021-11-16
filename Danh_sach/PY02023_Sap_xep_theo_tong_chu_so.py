def Sort_Tong_cs (a,n):
    a = sorted(a, key = lambda k :(Tong_cs(k), int(k)) )
    for i in a:
        print(i , end = " ")
    print()

def Tong_cs (n):    #n:str
    res = 0
    for i in n:
        res+= int(i)
    return res

t = int (input())
while t>0:
    n = int (input())
    a = input().split()
    Sort_Tong_cs(a,n)
    t-=1