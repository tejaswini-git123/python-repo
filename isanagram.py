def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase to handle case-insensitivity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

str1 = "hello World"
str2 = "worldolleh"
res = are_anagrams(str1, str2)
if res:
    print("Anagram words are the anagram")
else :
    print("Anagram words are not the anagram")



