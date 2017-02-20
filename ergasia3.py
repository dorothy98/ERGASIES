n = raw_input("Parakalw eisagete mia lista arithmwn. Oi arithmoi na einai xwrismenoi me keno: ")
numlist = n.split()
numlist = [int(a) for a in numlist] 
zeros = numlist.count(0)
while 0 in numlist:
 numlist.remove(0)
zerolist = [0] * zeros
numberlist = numlist + zerolist
print numberlist
