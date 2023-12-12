"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
"""
# method 1: Method 1 first converts the strings to sets, which removes duplicate characters. This is not necessary for checking anagrams, as anagrams should use all the original letters exactly once. Therefore, Method 1 may give incorrect results for some inputs.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(dict.fromkeys(s)))
        t = sorted(list(dict.fromkeys(t)))
        return t == s

# method 2: Method 2 is better than Method 1. The reason is that Method 2 is more straightforward and efficient. It directly sorts the strings and compares them, which is the essence of checking anagrams.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# test
s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s, t))