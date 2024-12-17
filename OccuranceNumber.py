t = (1,2,3,2,3,1,4)
j=0
c=1
dict1 = {}

for i in range(0,len(t)):
     if(i not in t):
        dict1.update(i,c)
     else:
         count = c+1
         dict1.update(i,count)

print(dict)