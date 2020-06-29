"""
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

"""
# my solution
def longest_palindrome(s):
    temp = ""
    substr = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            if temp != temp[::-1]:
                temp = ""
            if len(temp) > len(substr):
                substr = temp
    return len(substr)


print(longest_palindrome("abbbbc"))


# code wars
# solution 1
# def longest_palindrome(s):
#     for c in xrange(len(s), -1, -1):
#         for i in xrange(len(s) - c + 1):
#             if s[i:i + c] == s[i:i + c][::-1]:
#                 return c

# solution 2
# def longest_palindrome (s):
#     longest = 0
#     for left in xrange(len(s)):
#         for right in xrange(len(s), left, -1):
#             if s[left:right] in (s[left:right])[::-1]:
#                 longest = max(right-left, longest)
#                 break
#     return longest
