# user = {'Hovaten':'Nguyen Hoang Duong', 'MaSV': 'B19DCCN153', 'Class': 'D19CQCN09'}
# user ['monhoc'] = 'Python'
# print (user)

# lists = ['a', 1, 1 , 'a', 'b']
# res = {}
# for i in set(lists):
#     res[i] = lists.count(i)
# print (res)

# user = {'name':'A', 'age':20}
# for key, value in user.items():
#     print(f"Key:{key} - Value:{value} ")

# user = {'name':'A', 'age':20}
# for key in sorted(user.keys()):
#     print(key)

#Nesting:

# Dict = {1:'Python', 2:'For', 3:{'A':'Everybody', 'B':'Me', 'C':'You'}}
# print (Dict[3])

# print (len(Dict))

# info = {'A':1}
# Dict.update(info)
# print (Dict)

# res = {}
# for i in range(1,16):
#     res[i] = i**2
# print(res)

# dict = {'A':1, 'B':2, 'C':1.5}
# sum = 0
# for value in dict.values():
#     if type(value)==int or type(value) == float:
#         sum+=value
# print(sum)

d1 = {'a':1, 'b':2,'c':3}
d2 = {'a':3, 'b':2,'d':4}
d = d2
for key, value in d1.items():
    if key in d2.keys():
        d[key]= value + d2[key]
    else:
        d[key]=value
print(d)
    
def make_car(manufacture, model, **info_car):
    info_car['Hang xe'] = manufacture
    info_car['Kieu xe'] = model
    return info_car

car = make_car('huyndai','kona', color = 'blue', bks = '29A12345' )
print(car)
