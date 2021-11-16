def So_may_man(a,n,m):
    #Tim Mam, Min => SMM
    Max = Min = a[0][0]
    for i in range(0,n):
        for j in range(0,m):
            if a[i][j]>Max:
                Max = a[i][j]
            if a[i][j]<Min:
                Min = a[i][j]
    #Kiem tra xem co SMM khong
    flag = 0
    for i in range(0,n):
        for j in range(0,m):
            if a[i][j] == Max-Min:
                flag = 1
                break
        if flag==1:
            break
    #Print
    if flag==0:
        print("NOT FOUND")
    else:
        print(Max-Min)
        for i in range(0,n):
            for j in range(0,m):
                if a[i][j]==Max-Min:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
for i in range(0,n):
    a.append([int(x) for x in input().split()])
So_may_man(a,n,m)