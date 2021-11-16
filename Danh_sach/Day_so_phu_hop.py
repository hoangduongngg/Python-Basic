def DaySo_PhuHop(n,a,b):
    check = 0 #so cap so khong thoa man
    lists = [] #lists de hoan doi
    for i in range(0,n):
        if a[i] > b[i]:
            check +=1
            lists.append([a[i], b[i]])
            if check>2:
                return 0    
    
    if check==0:
        return 0
    elif check==1:
        return 1
    else:
        if (lists[0][0]<=lists[1][0] and lists[0][1]<=lists[1][1]) or (lists[0][0]>lists[1][0] and lists[0][1]>lists[1][1]):
            return 1
    return 0

t = int (input())
while t>0:
    n = int (input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if DaySo_PhuHop(n,a,b):
        print("YES")
    else:
        print("NO")
    t-=1
 