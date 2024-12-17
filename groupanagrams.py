from collections import defaultdict

def group_anagrams(strs):
    # Create a dictionary to hold lists of anagrams
    anagrams = defaultdict(list)

    # Iterate through each word in the input list
    for word in strs:
        # Sort the word and use the sorted word as the key
        sorted_word = ''.join(sorted(word))
        # Append the original word to the corresponding list in the dictionary
        anagrams[sorted_word].append(word)

    # Return all the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))