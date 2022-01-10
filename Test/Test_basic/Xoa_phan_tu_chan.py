s= [1,2,3,4,5,6]

# Cach 1: Dung while
# i=0
# while (i<len(s)):
#     if (s[i]%2==0):
#         s.pop(i)
#     i+=1
    
# Cach 1: Dung for
for i in s:
    if i%2==0:
        s.remove(i)
print(s)

sum, count = 0,0
for i in s:
    if (str(i).isnumeric()):
        sum+=i
        count+=1

print (sum, sum/count)