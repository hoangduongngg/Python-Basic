s  = [5,4,2,1,6,3]

#Cach 1:
bp = s
# j=0
# for i in s:
#     bp[j] = i*i #i**2
#     j+=1

#Cach 2:
bp = [i**2 for i in s]
bp_sorted = sorted (bp, reverse=True)
print(bp_sorted)