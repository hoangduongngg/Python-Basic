def Timso_NhoNhat (s):
    a = []
    i = 0
    while i<len(s):
        if '0'<= s[i] <= '9':
            tmp = ''
            while '0'<= s[i] <= '9':
                tmp += s[i]
                i+=1
                if i==len(s): break
            a.append(int(tmp))
        i+=1
    print(max(a))

t =int(input())
while t>0:
    Timso_NhoNhat(input())
    t-=1