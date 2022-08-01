class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n ** 2 <= x:
            n += 1
        return n - 1



# Runtime: 9891 ms, faster than 5.01% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14 MB, less than 11.09% of Python3 online submissions for Sqrt(x).


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            n = 1
            while n ** 2 <= x:
                n += 1000
            n -= 1000
            while n ** 2 <= x:
                n += 100
            n -= 100
            while n ** 2 <= x:
                n += 10
            n -= 10
            while n ** 2 <= x:
                n += 1      
            return n - 1



# Runtime: 51 ms, faster than 70.58% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.8 MB, less than 96.32% of Python3 online submissions for Sqrt(x).