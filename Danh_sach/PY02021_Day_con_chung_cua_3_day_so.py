def Day_con_chung(a,b,c):
    res = []
    i = j = k = 0
    while i<len(a) and j<len(b) and k<len(c):
        if a[i] == b[j] == c[k]:
            res.append(a[i])
            i,j,k = i+1, j+1, k+1
        elif a[i] < b[j]: i+=1
        elif b[j] < c[k]: j+=1
        else: k+=1
    if len(res)==0: print("NO")
    else:
        print(*res)
    

t = int (input())
while t>0:
    data = [int(i) for i in input().split()]
    n, m, k = data[0], data[1], data[2]
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    c = sorted([int(i) for i in input().split()])
    Day_con_chung(a,b,c)
    t-=1

# Input:

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output

# 20 80
# 5 5
# NO