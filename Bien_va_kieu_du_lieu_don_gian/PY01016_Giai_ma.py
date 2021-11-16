t = int (input())
while (t>0):
    s = input()
    for i in range(1,len(s),2):
        num = int (s[i])
        while num>0:
            print(s[i-1], end = "")
            num-=1
    print("\n")
    t-=1