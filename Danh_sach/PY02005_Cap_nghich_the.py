n = int (input())
a = input().split(" ")

count = 0
for u in range(0,n-1):
    for v in range(u+1,n):
        if int(a[u]) > int(a[v]):
            count+=1
print(count)