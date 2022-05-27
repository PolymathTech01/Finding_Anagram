# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):  # sorting the words and then comparing them
        return True
    else:
        return False


print(find_anagram('below', 'elbow'))
print(find_anagram('hello', 'check'))
