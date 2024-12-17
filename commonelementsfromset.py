
def common_elements(list1, list2):
    s1 =set(list1)
    s2 =set(list2)
    if(s1 & s2):
     print(s1 & s2)
    else:
     print("No common elements found")

list1 = [1,2,3,4,5]
list2 = [3,5,6,6,7]
common_elements(list1, list2)

s1 = set(list1)
s2 = set(list2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))






