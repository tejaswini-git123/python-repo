import json

f = open('data.json.txt')
data = json.load(f)
for i in data ['emp_details']:
    print(i)
f.close()
