import math
def PhanTich(n):
    print("1", end = " ")
    if (n%2==0):
        dem = 0
        while n%2==0:
            dem+=1
            n/=2
        print(f"* 2^{dem}", end=" ")
    for i in range(3,int(math.sqrt(n))+1,2):
        if (n%i==0):
            dem=0
            while n%i==0:
                dem+=1
                n/=i
            print(f"* {i}^{dem}", end= " ")
    
    if (n>1):
        print(f"* {int(n)}^1")
    print("\n")
        

t = int (input())
while t>0:
    n = int(input())
    PhanTich(n)
    t-=1