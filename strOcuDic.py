
def string_Ocurrance(str,x):
    dic = {}
    for i in str:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] =dic[i]+1
    return dic[x]
str = "swiss"
x = 's'
print(string_Ocurrance(str,x))








