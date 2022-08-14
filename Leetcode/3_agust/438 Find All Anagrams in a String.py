from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) :
        ans = []
        p_len = len(p)
        p = Counter(p)
        p_keys = p.keys()
        s_dict= Counter(s[0:p_len])
        print(s_dict)
        for i in range(p_len, len(s)):
            if s_dict == p :
                ans.append(i-p_len)
            s_dict = s_dict + Counter(s[i]) - Counter(s[i-p_len])
            print(s_dict)
        if s_dict == p:
            ans.append(len(s)-p_len)   
        return ans 


print(Solution.findAnagrams(Solution,s = "abab", p = "ab"))



# Runtime: 2781 ms, faster than 5.00% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 80.50% of Python3 online submissions for Find All Anagrams in a String.