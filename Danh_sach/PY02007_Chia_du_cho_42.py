import re
def Check(a): #a:list str
    for i in range(0,len(a)):
        a[i] = int(a[i])%42
    return len(set(a))
    
a = []
while len(a)<10:
    data = re.split(' +', input())
    a.extend(data)

print(Check(a))