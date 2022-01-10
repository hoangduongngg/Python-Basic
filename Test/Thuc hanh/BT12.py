lists = {'a':1, 'b':2, 'c':3}
for key, value in lists.items():
    max = min = value
    break

for key, value in lists.items():
    if value > max:
        max = value
    if value < min:
        min = value
print (min, max)