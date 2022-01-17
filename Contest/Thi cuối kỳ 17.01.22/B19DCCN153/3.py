import re

def Xuly_String(s):
    s = s.strip().lower()
    SpecialChar = re.compile('\W')
    s = re.sub(SpecialChar, " ", s)
    return s.split()


def Xuly(s1, s2):
    a = Xuly_String(s1)
    b = Xuly_String(s2)
    if len(a)==0 and len(b)==0:
        print(1)
    else:
        AB = 0
        for i in a:
            if i in b:
                AB += 1
        res = AB / (len(a) + len(b) - AB)
        print('%.2f'%res)


s1 = input().lower()
s2 = input().lower()

print (Xuly(s1, s2))
