class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        l1 = len(word1)
        l2 = len(word2)
        
        for ind in range(min(l1, l2)):
            ans += word1[ind]
            ans += word2[ind]
            
        if l1 == l2:
            return ans
        elif l1 > l2:
            for ind in range(l2, l1):
                ans += word1[ind]
            return ans
        elif l2 > l1 :
            for ind in range(l1, l2):
                ans += word2[ind]
            return ans


# Runtime: 47 ms, faster than 52.97% of Python3 online submissions for Merge Strings Alternately.
# Memory Usage: 13.9 MB, less than 69.59% of Python3 online submissions for Merge Strings Alternately.