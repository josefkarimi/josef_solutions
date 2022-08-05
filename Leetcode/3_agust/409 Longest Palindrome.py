class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        
        plus1 = 0
        ans = 0
        for n in letters.values():
            if n == 1:
                plus1 = 1
            elif n%2 == 0:
                ans += n
            else:
                ans += n - 1
                plus1 = 1
                
        return ans + plus1



# Runtime: 45 ms, faster than 67.99% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 14 MB, less than 22.89% of Python3 online submissions for Longest Palindrome.