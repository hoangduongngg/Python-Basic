def Check(s1, s2):
    if len(s1) != len(s2):
        return 0
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    for i in range(0, len(s1)):
        if s1[i]!=s2[i]:
            return 0
    return 1
    
    

t = int (input())
k=1
while t>0:
    s1, s2 = input(), input()

    print(f"Test {k}:", end = " ")
    k+=1
    if Check(s1,s2):
        print("YES")
    else:
        print("NO")
    t-=1