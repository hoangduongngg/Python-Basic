def Sap_xep(a,n,b):
    res = []
    chan = []
    le = []
    for i in a:
        if int(i)%2==0:
            chan.append(i)
        else:
            le.append(i)
    chan.sort
    le = sorted(le, reverse=True)
    j = k = 0
    for i in a:
        if int(i)%2==0:
            res.append(chan[j])
            j+=1
        else:
            res.append(le[k])
            k+=1
    #Print res
    i = 0
    while i<len(res):
        for j in b:
            temp = j
            while temp >0:
                print(res[i], end = " ")
                i+=1
                temp -=1
            print()

n = int (input())
a = []
b = [] #luu so luong so tung dong
while len(a)<n:
    lists = input().split()
    a.extend(lists)
    b.append(len(lists))

Sap_xep(a,n,b)