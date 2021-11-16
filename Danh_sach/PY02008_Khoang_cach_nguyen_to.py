import math
def SNT(n):
    if n==2:
        return 1
    if n%2 ==0 or n<2:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1

data = input().split(" ")
n, x = int(data[0]), int(data[1])
res = [x]
i= num = 0
while i<n:
    if SNT(num):
        res.append(res[i]+num)
        i+=1
    
    num+=1

for i in res:
    print(i, end = " ")

