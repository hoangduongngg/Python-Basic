def Run(s):
    if s[0]==s[-1]: print("YES")
    else: print("NO")

t = int(input())
while t>0:
    Run(input())
    t-=1