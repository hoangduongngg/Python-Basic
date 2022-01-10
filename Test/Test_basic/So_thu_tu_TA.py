# for n in range(1,10):
#     if n%10 == 1:
#         print(f'{n}st',end=' ')
#     elif n%10 == 2:
#         print(f'{n}nd',end=' ')
#     elif n%10 == 3:
#         print(f'{n}rd',end=' ')
#     else:
#         print(f'{n}th',end=' ')

res = []
for i in range(1,10):
    if i%10 == 1:
        res.append(f'{i}st')
    elif i%10 == 2:
        res.append(f'{i}nd')
    elif i%10 == 3:
        res.append(f'{i}rd')
    else:
        res.append(f'{i}th')
print(res)