import math
def Bien_doi(a):
    for i in range(0,len(a)):
        a[i] = int (a[i])
    count = 0

    while a.count(a[0])!=len(a):
        b = a.copy()
        for i in range(0,len(a)-1):
            b[i] = abs (a[i]-a[i+1])
        b[-1] = abs (a[-1]-a[0])
        count +=1 
        a=b.copy()
    return count

while 1:
    a = input().split(" ")
    if a.count('0')==4:
        break
    print (Bien_doi(a))