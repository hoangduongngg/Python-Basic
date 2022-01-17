t, k = map(int, input().split())
if t<0 or t>70 or k<0 or k>5: print("INVALID INPUT")
else:
    ds = []
    while t>0:
        a = input().split()
        dic = {'name':a[0], 'diem':int(a[1])}
        ds.append(dic)
        t-=1

    ds = sorted (ds, key= lambda k: (-k['diem'], k['name']))

    for i in ds[:k]:
        print(i.get('name') , end = " ")

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
