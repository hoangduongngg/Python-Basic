def Run(s):
    # s = "qwertyuiop"
    print(len(s))
    if len(s)>=3: print(s[-3:])
    s_ngc = s[::-1]
    for i in range(0, len(s)):
        if i%2==0: print(s_ngc[i], end = "")
    print()
    print(s[:-2])
    if len(s) >=5: print(s[:5])
    for i in range(0, len(s)):
        if i%2==0: print(s[i], end = "")
    print()
    
    for i in range(0, len(s)):
        if i%2==1: print(s[i], end = "")   
    print()
    print(s_ngc)
    if len(s)>=2: print(s[-2])

s = input()
Run(s)

# qwertyuiop