class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)
                
        res = []
        backtrack()
        return res

# not mine https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution

# Runtime: 61 ms, faster than 89.98% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 15.3 MB, less than 42.58% of Python3 online submissions for Letter Case Permutation.