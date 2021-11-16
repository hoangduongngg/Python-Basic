def So_thuan_nghich(n): #n:str
    n = str(n)
    if len(n)<2:
        return 0
    for i in range(len(n)//2):
        if n[i]!=n[-1-i]:
            return 0
    return 1

def So_thuan_nghich_max(a,n,m):
    Max = -1
    for i in range(0,n):
        for j in range(0,m):
            if So_thuan_nghich(a[i][j]) and a[i][j]>Max:
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

So_thuan_nghich_max(a,n,m)