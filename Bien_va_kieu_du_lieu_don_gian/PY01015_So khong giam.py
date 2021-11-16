t = int (input())
while t>0:
    str = input()
    n = len (str)
    i = 0
    while  i < n-1:
       a=int(str[i])
       b=int(str[i+1])
       if (a>b):
           print ('NO')
           break
       i+=1

    if (i==n-1):
        print ('YES')

    t-=1