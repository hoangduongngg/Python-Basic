# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

    # for line in file_object:
    #     print(line.rstrip())

# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

# print(f"{pi_string[:52]}...")

# file_name = 'programming.txt'
# with open (file_name, 'w') as file_object:
#     file_object.write("Something 123")

# file_name = 'programming.txt'
# with open (file_name, 'a') as file_object:
#     file_object.write("123")

#bai 1:
# file_name = 'guest.txt'
# with open (file_name, 'a') as file_object:
#     while 1:
#         name = input()
#         if name == "quit": break
#         file_object.write(name + '\n')

#bai 2:
# file_name = 'responses.txt'
# with open (file_name, 'a') as file_object:
#     while 1:
#         str = input()
#         if str == "": break
#         file_object.write(str + '\n')


import json
dict = {1:'a', 2:'b', 3:'c'}
#dict = dict(sorted(dict.items()))

filename = 'dict.json'
with open (filename, 'w') as f:
    json.dump(dict, f, indent=4, sort_keys=True)