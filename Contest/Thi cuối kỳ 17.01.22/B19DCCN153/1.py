def Run(s):
    s = s.lower()
    res = []
    for i in range(0, len(s)):
        if s[i]=='t': res.append(i)

    if len(res) ==0:
        print(-1)
    elif len(res) == 1:
        print(*res)
    else:
        print(res[0], res[1], res[-1])

t = int(input())
while t>0:
    Run(input())
    t-=1

# 4
# toiyeuPTIT
# CNTT1
# Python_Programing_Test_ptit
# chucmungnammoi