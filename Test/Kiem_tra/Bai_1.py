n = 153
for i in range(1,100+n+1):
    if i%3==0:
        print("Fizz", end = "")
        if i%5==0:
            print("Buzz")
        else:
            print()
    elif i%5==0:
        print("Buzz")
    else:
        print(i)