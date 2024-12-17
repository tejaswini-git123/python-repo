my_dict = {"Java": 100, "Python": 112, "C": 11}
value = 100

key = list(filter(lambda x : my_dict[x] == 100 , my_dict))
print(key)

x = "malayam"
w = ""
for i in x:
    w = i + w

if (x == w):
    print("IsPalindrome")
else:
    print("Not polindrome")


