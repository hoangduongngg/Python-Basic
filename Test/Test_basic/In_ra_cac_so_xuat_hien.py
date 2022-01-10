#in ra cac so xuat hien nhieu hon 3 lan
lists = [1,5,1,8,4,1,4,3,2,8,4,9]
res = []
for i in lists:
    if lists.count(i)>=3:
        res.append(i)
        
print(set(res))