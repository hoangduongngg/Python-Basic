def Xuat_hien_nhieu_nhat (a,n):
    res = []
    dem = []
    b = list(set(a))
    for i in b:
        dem.append(a.count(i))
    
    Max = max(dem)
    for i in range(0, len(dem)):
        if dem[i]==Max:
            res.append(b[i])
    return (min(res))
            

t = int (input())
while t>0:
    n = int (input())
    a = []
    while n>0:
        n-=1
        a.append(int(input()))
    print(Xuat_hien_nhieu_nhat(a,n))
    t-=1