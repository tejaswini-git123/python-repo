

def find_missing_number(list1,list2):
        sum_list1 = sum(list1)
        sum_list2 = sum(list2)
        return sum_list1 - sum_list2

list1 = [1,2,3,4,5]
list2 = [1,2,4,5]

missing_number = find_missing_number(list1,list2)
print(missing_number)