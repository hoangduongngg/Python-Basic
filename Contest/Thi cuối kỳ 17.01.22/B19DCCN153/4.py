import math

def Tinh_Vector (a,b):
    res = 0
    for i in range(0, len(a)):
        res += (a[i] - b[i])**2
    return math.sqrt(res)
def Xuly(ds,a):
    for i in ds:
        i['tinh'] = Tinh_Vector(a,i.get('vector'))
    ds = sorted(ds, key = lambda k: k['tinh'])

    print(ds[0].get('name'), end = " [")
    for i in ds[:-1]:
        print('%.4f'%i.get('tinh') , end = ", ")
    print('%.4f'%ds[-1].get('tinh') , end = "]")

N = int(input())
n = int(input())
a = [float(i) for i in input().split()]
ds = []
for i in range(0, N-3):
    s = input().split()
    x = [int(i) for i in s[1:]]
    ds.append({'name': s[0], 'vector':x})

if N<4 or n>1024:
    print("INVALID INPUT")
else:
    Xuly(ds, a)

# 6
# 3
# 0.9 0.07 0.03
# Ngan 1 0 0
# Minh 0 1 0
# Nhung 0 0 1