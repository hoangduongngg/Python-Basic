import math
def gcd_3so (a,b,c):
    if math.gcd(a,b)==1 and math.gcd(a,c)==1 and math.gcd(b,c)==1:
        return 1
    return 0

s = input().split(" ")
L,R = int(s[0]), int(s[1])
for i in range(L, R-1):
    for j in range(i+1, R):
        for k in range(j+1, R+1):        
            if gcd_3so(i,j,k):
                print(f"({i}, {j}, {k})")