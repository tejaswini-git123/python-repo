from array import *

arr = array('i', [])
n = int(input("Enter the length of an array"))

for i in range(n) :
    x = int(input("Enter the value of an array"))
    arr.append(x)

for i in arr :
    print(i)

search_value = int(input("Enter the value to search"))
# k = 0
# for e in arr :
#     if e==search_value :
#         print(k)
#         break
#     k+=1

for e in arr :
    if e==search_value :
        print(arr.index(e))
        break





