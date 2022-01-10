lists = ['www.abcdef.net', 'www.123456.com', 'www.ptithanoi.vn']
res=[]
for string in lists:
    res.append(string.split('.')[-1])

    
print(res)