def gt(n):
    if n<=1: return 1
    return n*gt(n-1)

def So_Krish(n):
    a = [int(i) for i in list(str(n))]
    if n==sum([gt(i) for i in a]):
        print("Yes")
    else: print("No")

t =int(input())
while t>0:
    So_Krish(int(input()))
    t-=1

# note: 0! = 1
# Input:
# 2
# 145
# 235

# Output:
# Yes
# No