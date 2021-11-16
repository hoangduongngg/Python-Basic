def Check(n):
    sum=0
    for i in range(0, len(n)):
        sum+= int(n[i])
    if sum%3==0:
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