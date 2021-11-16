import re
a = []
n = int(input())
while n>0:
    str = input()
    lists = re.split('?|!|-|, |\*|\n', str)
    a.extend(lists)
    n-=1
print(a)

#,|.|?|!|:|;|(|-|/