a = [1,2,3,4,5,6,7,8,9]
chan= le = 0
for i in a:
    if i%2==0:
        chan+=1
    else:
        le+=1
print (chan, le)