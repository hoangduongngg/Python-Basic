def Ktra_XauThangBang (s):
    s2 = s[::-1]
    for i in range(0, int(len(s)/2)):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(s2[i]) - ord(s2[i+1])): return 0
    return 1

def Check(s):
    if Ktra_XauThangBang(s): print("YES")
    else: print("NO")
    
t = int(input())
while t>0:
    Check(input())
    t-=1

# 2
# acxz
# bcxz