class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p%2 == 0 and q%2 == 0:
            p = p//2
            q = q//2
        if p%2 == 0 :
            return 2
        else:
            if q%2 == 1 :
                return 1
            else :
                return 0



# Runtime: 51 ms, faster than 45.54% of Python3 online submissions for Mirror Reflection.
# Memory Usage: 14 MB, less than 16.83% of Python3 online submissions for Mirror Reflection.