import math
def Ktra(a,n,m):
    for i in range(0,n):
        for j in range(0,m):
            if SNT(int (a[i][j])):
                print("1", end = " ")
            else:
                print("0", end = " ")
        print()

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
n = int (data[0])
m = int (data[1])
a = []
for i in range(0,n):
    a.append(input().split())
Ktra(a,n,m)
