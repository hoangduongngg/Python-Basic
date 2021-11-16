def Tach_so(s):
    res = []
    temp = ''
    for i in s:
        if i.isnumeric():
            temp+=i
        elif temp!='':
            res.append(int(temp))
            temp = ''
    if temp!='':
        res.append(int(temp))
    return res

t = int(input())
num = []
while t>0:
    num.extend(Tach_so(input()))
    t-=1
for i in sorted(num):
    print(i)