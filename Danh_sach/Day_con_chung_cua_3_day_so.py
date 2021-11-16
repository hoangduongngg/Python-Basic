def Day_con_chung(n,m,k,a,b,c):
    res = []
    for i in a:
        for j in b:
            if j>i:
                break
            elif i==j:
                for k in c:
                    if k>i:
                        break
                    elif i==k:
                        res.append(i)
                        break
                break

    if len(res)==0:
        print("NO")
    else:
        for i in res:
            print(i, end = ' ')
        print()

t = int (input())
while t>0:
    data = [int(i) for i in input().split()]
    n, m, k = data[0], data[1], data[2]
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    c = sorted([int(i) for i in input().split()])
    Day_con_chung(n,m,k,a,b,c)
    t-=1