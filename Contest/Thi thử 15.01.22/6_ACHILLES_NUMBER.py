import math
def Strong_number (n):
    dic = {}
    if n%2==0:
        dic[2] = 0
        while n%2==0:
            dic[2]+=1
            n = int(n/2)
    for i in range(3,int(math.sqrt(n))+1, 2):
        if n%i==0:
            dic[i] = 0
            while n%i==0:
                dic[i]+=1
                n = int(n/i)
    if n!=1: dic[n] =1

    for i in dic:
        if dic.get(i) <2: return 0
    return 1

def Perfect_number (n):
    a = []
    for i in range(1, n):
        if n%i==0:
            a.append(i)
    
    if (sum(a) == n): return 1
    return 0

def Xuly(n):
    if Strong_number(n)==1 and Perfect_number(n)==0: return 1
    return 0
        

n = int(input())
print(Xuly(n))