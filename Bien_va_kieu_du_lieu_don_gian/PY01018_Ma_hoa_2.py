P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
    data = input()
    lists = data.split(" ")
    K = int (lists[0])
    if (K==0):
        break
    s = lists[1]
    res = []
    for i in s:
        res.append(P[(P.find(i) + K)%28])
    for i in list(reversed(res)):
        print(i, end="")
    print("\n")