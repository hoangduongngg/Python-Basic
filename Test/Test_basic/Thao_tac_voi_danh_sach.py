str = ['Hello','Python', 'Programming', 'PTIT']
str.pop()
print (str)

str.insert (3, '2021')
print (str)

str[0]='Python'
print (str)


temp = str[0]
str[0]=str[-1]
str[-1]=temp

print(str)