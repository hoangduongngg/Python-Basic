def Dayso_2cs(n):
    res = []
    for i in range(0, len(n)-1, 2):
        res.append(n[i]*10 + n[i+1])
    
    temp = list(set(res))
    for i in res:
        if i in temp:
            print(i, end = " ")
            temp.remove(i)

n = [int(i) for i in list(input())]
Dayso_2cs(n)