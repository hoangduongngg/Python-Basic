str = input()
#str = str.strip
i, n = 0, len(str)
#bien first de gan vi tri dau tien cua tu
first = 0
while i<n:
    if (str[i]==' ' ):
        print (str[first:i])
        first = i+1
    i+=1
print (str[first:n])