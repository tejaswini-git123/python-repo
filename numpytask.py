from numpy import *
arr = array([1,2,3,4])
arr1 = array([3,5,6,7])
# arr3 = arr+arr1
# print(arr3)
arr3 = arr
print(arr3)

def my_function(country = "India") :
    print("I am for " + country)

my_function()
my_function("Swedan")
my_function("Norway")

def my_function1(fname,Lastname) :
    print(fname + " " + Lastname)

my_function1("Hello","World")
my_function1(fname ='teju',Lastname = 'niki')
def my_function2(child1 , child2 , child3 ) :
    print("the yougest child : " + " " + child3)
my_function2 ("Hi" , "Hello" , "Fun")

def my_function2(*kids) :
    print("Yougest child : " + kids[1])
my_function2("hh" , "fff" , "jj")

def printinfo(name,age = 35) :
    print("Name : " + name)
    print("Age : " + str(age))
    return
printinfo("niki")
printinfo("niki" , age = 50)







