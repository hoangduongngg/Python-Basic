Lists = ['a','b']
res= []
n = 4
for list in Lists:
    for i in range(1,n+1):
        res.append(list + str(i))
print (res)