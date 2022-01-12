def SNT(n):
    if n==2: return 1
    if n<2 or n%2==0: return 0
    i=3
    while i*i<=n:
        if n%i==0: return 0
        i+=2
    return 1
def Perfect_Prime(n):
    if not SNT(n): return 0
    n = str(n)
    if not SNT(int(n[::-1])): return 0
    if not SNT(sum(map(int, list(n)))): return 0
    for i in n:
        if not SNT(int(i)): return 0
    return 1

def Check(n):
    if Perfect_Prime(n): print("Yes")
    else: print("No")

t = int(input())
while t>0:
    Check (int(input()))
    t-=1

# Input:

# 3
# 13
# 753
# 757
# Output:

# No

# No

# Yes