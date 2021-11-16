def SMM(n):
    for i in n:
        if (i!='4' and i!='7'):
            return 0
    return 1

t = int (input())
while t>0:
    n = input()
    if SMM(n):
        print("YES")
    else:
        print("NO")
    t-=1