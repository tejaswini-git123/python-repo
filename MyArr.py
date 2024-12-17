import array

values = array.array('i',[1,2,2,3,4,5])
values.reverse()

print(values.typecode)
newval = array.array(values.typecode,(a for a in values))

i = 0

while i<len(newval) :
    print(newval[i])
    i+=1


