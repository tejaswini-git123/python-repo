def count_ocurrance(tup,x) :
    dict1 = {}

    for elements in tup:
        if elements not in dict1:
            dict1[elements] = 1
        else:
            dict1[elements] = dict1[elements] + 1
    return dict1[x]

tup = (1,2,3,2,4,3,1,4,44,3,3)
res = 3
numOccurance = count_ocurrance(tup,res)
print(numOccurance)
