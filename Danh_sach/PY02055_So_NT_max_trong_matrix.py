import math
def SNT(n):
    if n==2:
        return 1
    if n%2 ==0 or n<2:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1

def SNT_max(a,n,m):
    Max = -1
    for i in range(0,n):
        for j in range(0,m):
            if SNT(a[i][j]) and a[i][j]>Max:
                Max = a[i][j]
    if Max==-1:
        print("NOT FOUND")
    else:
        print(Max)
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j]==Max:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
for i in range(0,n):
    a.append([int(x) for x in input().split()])
SNT_max(a,n,m)