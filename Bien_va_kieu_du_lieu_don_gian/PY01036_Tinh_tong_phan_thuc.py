def Tong_phan_thuc(n):
    res=0
    if n%2:
        k=1
    else:
        k=2
    for i in range(k, n+1, 2):
        res += 1/i
    #print(round(res,6))
    print ("{:.6f}".format(res))

t = int (input())
while t>0:
    n = int(input())
    Tong_phan_thuc(n)
    t-=1