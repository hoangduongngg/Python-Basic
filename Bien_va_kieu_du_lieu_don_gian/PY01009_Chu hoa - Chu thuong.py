str = input()
i,n = 0, len(str)
chuthuong, chuhoa = 0,0
while i<n:
    if ('a'<=str[i]<='z'):
        chuthuong+=1
    if ('A'<=str[i]<='Z'):
        chuhoa+=1
    i+=1
if (chuthuong>=chuhoa):
    print (str.lower())
else:
    print (str.upper())