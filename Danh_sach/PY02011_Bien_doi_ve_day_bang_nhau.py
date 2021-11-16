def Biendoi(a,n):
    res = []
    for i in a:
        temp = 0
        for j in a:
            temp +=abs(j-i)
        res.append(temp)

    print(f"{min(res)} {a[res.index(min(res))]}")

n = int (input())
a = [int(i) for i in input().split()]
Biendoi(a,n)