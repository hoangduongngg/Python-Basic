def Xuly(s):
    a = s.split()
    n = len(a)

    ds = []
    for i in set(a):
        TF = a.count(i)/n
        dic = {'word':i, 'TF':TF}
        ds.append(dic)
    
    ds_sort =  sorted(ds, key= lambda k: (-k['TF'], k['word']))
    Max = ds_sort[0].get('TF')
    Max2=0
    for i in ds_sort:
        if i.get('TF')<Max:
            Max2 = i.get('TF')
            break
    for i in ds_sort:
        if i.get('TF')==Max2:
            print(i.get('word'), end=" ")
        elif i.get('TF') <Max2:
            break

t = int(input())
s = ""
while t>0:
    s+= input() + " "
    t-=1
Xuly(s)

# 4
# apple orange banana
# banana orange fruit
# mango orange
# mango