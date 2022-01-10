n = 5
print("tam giac vuong")
for i in range(0,n):
    print('*'*(2*i+1) )

n = 5
print("tam giac vuong 2")
for i in range(0,n):
    print(' '*(2*(n-1-i)+1) + '*'*(2*i+1) )

n = 5
print("tam giac can")
for i in range(0,n):
    print(' '*(n-1-i) + '*'*(2*i+1) )

n = 5
print("tam giac can nguoc")
#thap nguoc
for i in range(0,n):
    print(' '*(i) + '*'*(2*(n-1-i)+1) )

print("hinh chu nhat")
n,m = 2,3
for i in range(0,n):
    for j in range(0,m):
        print('*', end = '')
    print()


