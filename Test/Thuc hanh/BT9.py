string = 'progamming'
lists=[]
for i in string:
    lists.append(i)
    
res = {}
for i in set(lists):
    res[i] = lists.count(i)
print (res)