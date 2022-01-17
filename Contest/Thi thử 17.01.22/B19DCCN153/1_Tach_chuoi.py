s = input().split()
a = []
for i in s:
    dic = {'word':i, 'len':len(i)}
    a.append(dic)
a = sorted(a, key=lambda k : (-k['len'], k['word']))
Max = a[0].get('len')
Min = a[-1].get('len')

for i in a:
    if i.get('len') ==Max or i.get('len')==Min:
        print(i.get('word'), i.get('len'))

# Hom nay thi cuoi ky mon Lap trinh Python 