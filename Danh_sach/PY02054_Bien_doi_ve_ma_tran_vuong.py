def Bien_doi(n,m,a):
    if n==m:
        for i in a:
            print(*i)
    elif n>m:
        res = []
        for i in range(0,n):
            res.append([a[i], i])
        for i in res:
            if len(res) == m:
                break
            if i[1]%2==0:
                res.remove(i)
        for i in res:
            print(*i[0])
    #m>n
    else:
        res = []
        for i in range(0,n):
            res.append([])
            j = k = 0
            while j<m:
                if k<m-n:
                    if j%2==0:
                        res[i].append(a[i][j])
                    else:
                        k+=1
                else:
                    res[i].append(a[i][j])

                j+=1
        for i in res:
            print(*i)
                
n,m = map(int, input().split())
a = []
for i in range(0,n):
    a.append(input().split())
Bien_doi(n,m,a)
