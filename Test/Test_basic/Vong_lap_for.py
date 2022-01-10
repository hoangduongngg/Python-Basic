# s = [ 'a','b', 'c']
# for i in s:
#     print(f"{i.title()}, hello")

# #in ra tu 1 - 4:
# for value in range(1,5):
#     print(value)

# numbers = list (range(1,5))
# print (numbers)

#list cac so tu 2-10 cach nhau 2 don vi
# numbers = list (range(2,11,2))
# print (numbers)

# squares = []
# for value in range(1,11):
#     squares.append(value**2)

squares = [ value**2 for value in range(1,11)]
print(squares)
print(min(squares), max(squares), sum(squares))
