"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
import string

# my solution
def is_pangram(s):
    if len("".join(set([letter.lower() for letter in s if letter.isalpha()]))) == 26:
        return True
    return False


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))


# codewars solution 1
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


# # codewars solution 2
# def is_pangram(s):
#   if len(s) <= 28:
#     return False
#   return True
