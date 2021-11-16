def Xuat_hien_nhieu_nhat (a,n):
    for i in set(a):
        if a.count(i)>int(n/2):
            return i
    return "NO"

t = int(input())
while t>0:
    n = int (input())
    a = [int(i) for i in input().split()]
    print(Xuat_hien_nhieu_nhat(a,n))
    t-=1