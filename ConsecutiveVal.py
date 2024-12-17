from collections import OrderedDict

str = 'AABCAAADA'
k=3
for index in range(0,len(str),k):
    print(str[index:index+k])

