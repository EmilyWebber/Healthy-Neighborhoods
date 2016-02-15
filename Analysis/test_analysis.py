l = [9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in l:
    if type(i) != float:
        print ("Found an integer")
    else:
        print (type(i))

l.sort()

print (len(l)/3)

print (min(l))