def Lam_tron(n):
    n = [int(x) for x in list(reversed(n))]
    for i in range(0,len(n)-1):
        if n[i]>=5:
            n[i+1]+=1
        n[i]=0

    for i in list(reversed(n)):
        print(i, end = "")
    print()

t = int (input())
while t>0:
    n = input()
    Lam_tron(n)
    t-=1