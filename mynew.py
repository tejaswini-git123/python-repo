import sys
print(sys.version)

x,y,z = 'red','orange','blue'
print(x,y,z)
print(x+y+z)
print(x)
print(y)
print(z)
x=y=z=2
print(x,y,z)
a=1
b=2.8
c=1j
x=int(b)
y=int(a)
z=complex(a)
print(x,y,z)
s = "Python"
print(s)
print(s[0])
print (s[1:3])
print(s[::-1])
s1 = 'Hi' +" " + s[0:6]
print(s1)
print(len(s))
t = (1,2,3,4)
print(t)
print(t[1])
print(t[1:])
t1 = ('a','b','c')
t2 = t + t1
print(t2)
print(t2[1])
print(t2[-1])
print(t*2)
t3= (t1,t2)
print(t3)
print(t3[1][0])
a = [1,'e',4]
x = tuple(a)
print(x)
for x in t :
    print(x)
a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']
c = [1, 'hello', 3.14, True]
d = [1,2.4,'true',[1,2]]
print(a)
print(b)
print(c)
print(d[3][1])
friuts = ["apple","orange","red"]
x,y,z = friuts
print(x,y,z)
t5 = (1, 2, 3, 'apple', 4.5)
# From a tuple
a = list(t5)
print(a)
a = [2] * 5
b = [0] * 7
print(a)
print(b)
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[-1])
print(a[0:3])

a = []
a.append(10)
print("After append(10):", a)
a.append(26)
print("After append(26):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)
a.insert(1,20)
print("After insert(1, 2):", a)

a.extend([15,34,12])
print("After extend :", a)

#update element
a = [10, 20, 30, 40, 50]

a[1] = 25

print(a)

a = [10, 20, 30, 40, 30, 50]

# Removes the first occurrence of 30
a.remove(30)
print("After remove(30):", a)
# Removes the element at index 1 (20)
popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)
# Deletes the first element (10)
del a[0]
print("After del a[0]:", a)

a = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in a:
    print(item)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[2][1])

s = {1,'s',3,3}
print(s)
s1 = set([1,2,3,2])
print(s1)
t = ("Python", "is", "awesome")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with the use of a dictionary
d = {"Python": 1, "for": 2, "Python": 3}
print("\nSet with the use of Dictionary: ")
print(set(d))

set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

# Creating a Set with a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Python', 4, 'For', 6, 'Python'])
print("\nSet with the use of Mixed Values")
print(set1)

set2 = set()
d={"python":1 , "Awesome": 2}
print(set2)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing elements from Set  using Remove() method
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)

set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)

set1.clear()
print(set1)

d = {"python" : 1 , "Awesome" : 2}
print(d)
print(d.get("python"))
d = {'Dict1': {1 : "Python",'Nested1' : {11 : "Yes"}},'Dict2' :{'Name': 'for'}}
print(d)
print(d['Dict1'])
print(d['Dict1']['Nested1'][11])
print(d['Dict2']['Name'])
print(d.get('Dict2'))

d = {1: 'Python', 'name': 'For', 3: 'Python'}
print(d.items())
print(d.keys())
print(d.values())


print("Dictionary =")
print(d)
del(d[1])
print("Data after deletion Dictionary=")
print(d)








