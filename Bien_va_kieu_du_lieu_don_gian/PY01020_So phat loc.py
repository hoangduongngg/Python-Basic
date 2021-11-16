t = int (input())
while t>0:
    n = int (input())
    if (n%10 == 6):
        n//=10
        if (n%10 == 8):
            print ('YES')
        else:
            print ('NO')
    else:
        print ('NO')
    t=t-1