def Dayso_2cs(n,k):
    res = []
    flag = 0
    for i in range(0, len(n)-1, 2):
        res.append(n[i]*10 + n[i+1])
    for i in sorted(list(set(res))):
        if res.count(i)>=k:
            flag = 1
            print(f"{i} {res.count(i)}")
    if flag==0:
        print("NOT FOUND")

n = [int(i) for i in list(input())]
k = int (input())
Dayso_2cs(n,k)