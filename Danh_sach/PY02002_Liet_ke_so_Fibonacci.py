def Fibonacci(a,b):
    f = [0,1,1]
    for i in range(3, 93):
        f.append(f[i-1]+f[i-2])
    
    for i in range(a,b+1):
        print(f[i], end = " ")
    print()

t = int (input())
while t>0:
    data = input().split()
    a, b = int (data[0]), int (data[1])
    Fibonacci(a,b)
    t-=1