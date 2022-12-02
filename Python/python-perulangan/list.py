list1 = ["a","b","c","d","e"]
list1[4]="z"
list1.append('f')
list1.append('g')
del list1[6]
#print (list1)
#print (list1[2])
#print (list1[-3])
#print (list1[1:])

#for x in list1:
#    print (x, "", end ="")
x=0
while ( x < len(list1)):
    print (list1[x], "", end = "")
    x=x+1
