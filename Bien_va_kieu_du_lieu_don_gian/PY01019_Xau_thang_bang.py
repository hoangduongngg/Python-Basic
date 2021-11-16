import math
def Check(s):
    for i in range(0,len(s)-1):
        if ( abs(ord(s[i]) - ord(s[i+1])) != abs(ord(s[-1-i])- ord(s[-2-i])) ):
            return 0
    
    return 1

t = int (input())
while t>0:
    s = input()
    if Check(s):
        print("YES\n")
    else:
        print("NO\n")
    t-=1