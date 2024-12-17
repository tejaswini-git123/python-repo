tuple1=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
x=list(filter(lambda i: (i==10),tuple1))
print("the element 10 occurs",len(x),"times")


def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count

# Driver Code
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
renq = 4
renq1 = 10
renq2 = 8

print(countX(tup, renq))
print(countX(tup, renq1))
print(countX(tup, renq2))



