def So_thuan_nghich(n):
    n = str(n)
    for i in range(0, int(len(n)/2)):
        if n[i]!=n[-1-i]:
            return 0
    return 1
def Check(n):
    n = str(n)
    for i in n:
        if int(i)%2==1:
            return 0
    return 1

t = int (input())
while t>0:
    n = int (input())
    i=10
    while i<n:
        if len(str(i))%2==1:
            i*=10
            if i>n:
                break
        if So_thuan_nghich(i) and Check(i):
            print(i, end = " ")

        i+=2
    print()
    t-=1