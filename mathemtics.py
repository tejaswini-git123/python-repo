import math
x = math.sqrt(25)
print(x)
print(math.floor(2.8))
print(math.ceil(2.3))
print(math.pow(3,2))
print(math.pi)

num = 3

for i in range(2,num) :
    if(num % i ==0) :
        print("Not prime")
        break;
else :
    print("prime")