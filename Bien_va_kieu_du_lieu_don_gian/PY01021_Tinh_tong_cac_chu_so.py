def Tong_cs_xau(s):
    num = []
    for i in s:
        if '0'<=i<='9':
            num.append(i)
    for i in num:
        s.remove(i)
    num = [int(i) for i in num]
    print(f"{''.join(sorted(s))}{sum(num)}")

t = int(input())
while t>0:
    s = list(input())
    Tong_cs_xau(s)
    t-=1