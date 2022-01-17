def Run(a):
    if len(a) == 0:
        print('0 0')
    else:
        res = [a[0]]
        for i in range(1, len(a)):
            res.append(res[-1] + a[i])

        Tich = 1
        for i in res:
            Tich *= i

        print(sum(res), Tich)

t = int(input())
a = [int(i) for i in input().split()]

Run(a)