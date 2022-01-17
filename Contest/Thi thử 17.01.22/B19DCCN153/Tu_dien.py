t = int(input())
if t<0 or t>10:
    print("INVALID INPUT")
else:
    res = []
    while t>0:
        a = input().split()
        for i in a:
            try:
                res.append(int(i))
            except:
                continue
        
        t-=1

    # print(*res)
    Tich = 1
    for i in res:
        Tich *= i
    print(sum(res), Tich)

# 4
# a 9
# b 5
# c abc
# d 1