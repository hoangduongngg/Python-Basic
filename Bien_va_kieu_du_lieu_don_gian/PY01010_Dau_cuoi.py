def Check(n):
    if (len(n)<4 or len(n)>18):
        return 0
    a = int(n[0])*10 + int(n[1])
    b = int(n[-2])*10 + int(n[-1])
    if a==b:
        return 1
    return 0

t = int (input())
while t>0:
    n = input()
    if Check(n):
        print("YES")
    else:
        print("NO")
    t-=1