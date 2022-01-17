k = int(input())
res = []
while k>0:
    s = input().split()
    try:
        res.append(int(s[1]))
    except:
        None
    k-=1

if k<0 or k>10:
    print("INVALID INPUT")
else:
    Tich = 1
    for i in res:
        Tich *= i
    print(sum(res), Tich)

# 4
# a 9
# b 5
# c abc
# d 1