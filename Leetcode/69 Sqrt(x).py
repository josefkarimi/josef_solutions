class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n ** 2 <= x:
            n += 1
        return n - 1



# Runtime: 9891 ms, faster than 5.01% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14 MB, less than 11.09% of Python3 online submissions for Sqrt(x).