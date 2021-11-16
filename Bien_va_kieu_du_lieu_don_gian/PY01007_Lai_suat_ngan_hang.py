t = int(input())
def LaiSuat (n,x,m):
    i = 0
    while n<m:
        i+=1
        n += n*x/100
    return i


while t>0:
    data = input()
    a = data.split(" ")
    n,x,m = float (a[0]),float (a[1]),float (a[2])
    print(LaiSuat(n,x,m))

    t-=1