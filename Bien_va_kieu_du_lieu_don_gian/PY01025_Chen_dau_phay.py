s = input()
n = len(s)
res = []
s = list(reversed(s))
for i in range(0, n):
    if i%3==2 and i<n-1:
        res.append("," + s[i])    
    else:
        res.append(s[i])

for i in list(reversed(res)):
    print(i, end = "")
