import math

s = input().split(" ")
n,k = int(s[0]), int(s[1])
dem = 0
for i in range( int(math.pow(10,k-1)), int(math.pow(10,k))):
    if math.gcd(n,i)==1:
        if dem<10:
            dem+=1
            print(i, end=" ")
            if dem==10:
                print()
                dem=0