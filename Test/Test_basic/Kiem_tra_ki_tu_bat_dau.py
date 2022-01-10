lists = ['a', 'p','python', 'papa', 'PTIT', 'P', 'hello']
res = []
for string in lists:
    if string.startswith('py') or string.startswith('P'):
        res.append(string)
print (res)