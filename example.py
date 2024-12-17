from collections import defaultdict
test_list = ['lump','eat','me','tea', 'em', 'plum']
temp = defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())
print(res)

d = {'lump' : ['plum' , 'mplu'] , 'eat' : 'f'}
d['lump'].append('xxx')

str = "soreet"
str1 = "rtosee"
if (sorted(str) == sorted(str1)):
    print("yes")
else:
    print("no")
