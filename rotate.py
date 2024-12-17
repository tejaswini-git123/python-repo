
def rotate(list,n) :
    if n > len(list) :
         n = int(n % len(list))

    return list[-n:] + list[:-n]

list = [1,2,3,4,5,7,8]
rotated = rotate(list ,10)
print(rotated)

print(dict.fromkeys(list))


