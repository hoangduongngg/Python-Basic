n = int (input())
a = input().split()
count=0
for i in range(0,n-1):
    if a[i]!=a[i+1]:
        count+=1
print(count)