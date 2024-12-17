def IsPalindrome(s):
    return s == s[::-1]
s="malayalam"
res = IsPalindrome(s)
if res:
    print("ispalindrom")
else  :
    print("Not palindrom")

str = "zoho"
w = ""
for i in str:
     w = i + w
if (str == w):
    print("Ispalindrom")

else :
    print("Not palindrom")


l = [1,2,3,4]
l.insert(1,3)
print(l)

d = {1 : "greeks" , 2 : 'for' , 'age' : 22}
print(d.keys())
print(d.values())
print(d.items())

d1 = {'Geek': 1, 'for': 2, 'Geeks': 3}
res = "_".join(d1)
print(res)



