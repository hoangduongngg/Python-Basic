numbers = [5,0, 150,50,2,10,60]
res = []
for i in numbers:
    if i >= 150:
        break
    elif i%5 == 0:
        res.append(i)
print (res)