def Xuly(ds, k):
    ds = sorted(ds, key= lambda k:(-k['diem'], k['name']))
    for i in ds[:k]:
        print(i.get('name'), end = ' ')

n, k = map(int, input().split())
ds = []
for i in range(0,n):
    s = input().split()
    ds.append({'name':s[0], 'diem': int(s[1])})

if n<0 or n>70 or k<0 or k>5:
    print("INVALID INPUT")
else:
    Xuly(ds, k)


# 10 3
# Hung 6
# Long 7
# Giang 8
# Linh 5
# Tuan 8
# Hoa 9
# Mai 5
# Ngoc 4
# Khanh 9
# Ngan 10