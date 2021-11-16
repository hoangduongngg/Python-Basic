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
#tao 1 list SNT
list_NT = []
for i in range(0, 10001):
    if SNT(i):
        list_NT.append(i)

t = int (input())
a = [int(i) for i in input().split()]
res = 0
for i in a:
    if SNT(i)==0:
        for j in range(0, len(list_NT)):
            if list_NT[j] < i < list_NT[j+1]:
                res += min( i-list_NT[j], list_NT[j+1]-i)
print(res)