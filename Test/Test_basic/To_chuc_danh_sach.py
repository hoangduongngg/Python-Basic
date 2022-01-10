s= ['b','c','a','d','e']
num = [2,0,2,1]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

print(len(s))

s_sorted = sorted(s,reverse=True)
print(s_sorted) #khong lam thay doi vi tri danh sach ban dau

list = s+num*2
print (list)

