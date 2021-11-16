def Tich_cs_le(n):
    flag = 0
    res = 1
    for i in range(1, len(n),2):
        if n[i]!='0':
            flag = 1
            res*=int(n[i])
    if flag==0:
        return 0
    return res

def Tong_cs_chan(n):
    sum = 0
    for i in range(0, len(n),2):
        sum+=int(n[i])
    return sum

t = int(input())
while t>0:
    n = input()
    print(f"{Tong_cs_chan(n)} {Tich_cs_le(n)}")
    t-=1