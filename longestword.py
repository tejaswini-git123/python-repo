def longest_word(input_string):
    words = input_string.split()
    longest = max(words, key=len)
    return longest

str = "python is awesome"
res = longest_word(str)
print(res)