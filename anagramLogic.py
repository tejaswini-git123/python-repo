s1 = "dad"
s2 = "addd"

char_list_1 = list(s1)
char_list_2 = list(s2)

dic ={}

for char in char_list_1:
    if char not in dic:
        dic[char] = 0
    dic[char] += 1
for char in char_list_2:
    if char not in dic:
        print("The strings are not anagrams.")
        break
    dic[char] -= 1
else :
    for count in dic.values():
        if count!=0 :
            print("The strings are not anagrams.")
            break
    else :
        print("Strings are anagrams.")