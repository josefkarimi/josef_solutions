class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while n**2 < num:
            n += 1
        return n ** 2 == num



# Runtime: 94 ms, faster than 5.10% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 13.8 MB, less than 56.42% of Python3 online submissions for Valid Perfect Square.