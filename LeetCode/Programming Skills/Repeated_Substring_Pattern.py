"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.



Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
# Attempt 1: missread the question if followed the key word in question i would have solved it
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         list_a = []
#         list_b = []
#         for i in range(len(s)):
#             if s[i] not in list_a:
#                 list_a.append(s[i])
#                 print("list_a:", list_a)
#             elif s[i] in list_a:
#                 list_b.append(s[i])
#                 print("list_b:", list_b)
#             if len(list_b) == len(list_a):
#                 break
#         print("list_a:", list_a)
#         print("list_b:", list_b)
#         if list_a == list_b:
#             return True
#         else:
#             return False

# method 2: got the help from the web, it is a nw syntax for me so i got to learn a new thing today >3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
# test
s = "ababba"
print(Solution().repeatedSubstringPattern(s))
