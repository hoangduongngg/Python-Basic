import re
# word = []
# s = input().lower()
# word.extend(re.findall(r'[a-zA-Z]+', s))

s = 'abc d a'
x = re.findall('[a-zA-Z]+', s) #list
print(x)