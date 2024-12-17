def removeDupliacte(a) :
    return list(dict.fromkeys(a))
a = [1,2,2,3,4,1,4]
result  = removeDupliacte(a)
print(result)

b = [1,2,2,3,4,1,4]
res = []
for val in b :
    if val not in res :
        res.append(val)

print(res)
