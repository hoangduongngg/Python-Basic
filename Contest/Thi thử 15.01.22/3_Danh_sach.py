ds = []
t = int(input())
while t>0:
    ds.append(input().lower())
    t-=1

a = list(set(ds))
a = sorted(a)
for i in a:
    print(i)

# 5
# nguyenmanhson
# sonnm
# NGUYENMANHSON
# SonNM
# NguyenManhSon