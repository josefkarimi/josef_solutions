class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return (s == t)


# Runtime: 97 ms, faster than 22.87% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 11.53% of Python3 online submissions for Valid Anagram.




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        for letter in s:
            try:
                t.remove(letter)
            except:
                return False
        return True



# Runtime: 1050 ms, faster than 5.04% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 21.28% of Python3 online submissions for Valid Anagram.