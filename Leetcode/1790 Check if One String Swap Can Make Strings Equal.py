class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for k in range(len(s2)):
            if s1[k] != s2[k]:
                diff.append(k)
        if len(diff) == 0:
            return True
        elif len(diff) == 2:
            if s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]: 
                return True
            else:
                return False
        else:
            return False


# Runtime: 33 ms, faster than 90.45% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
# Memory Usage: 13.9 MB, less than 72.60% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.