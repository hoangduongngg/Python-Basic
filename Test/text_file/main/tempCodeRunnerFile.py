file_name = 'guest.txt'
with open (file_name, 'a') as file_object:
    while 1:
        name = input()
        if name == "quit": break
        file_object.write(name + '\n')