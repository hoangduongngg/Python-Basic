Lists = [[1,2,3], [4,5,6],[10,11,12]]
max=0
for list in Lists:
    sum = 0
    for i in list:
        sum+=i
    if sum>max:
        max=sum
        res = list
print(res)

#cach 2:
# Sum = [sum(i) for i in Lists]
# index_res = Sum.index(max(Sum))
# res = Lists[index_res]
# print(res)