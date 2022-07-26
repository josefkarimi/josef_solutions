class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for n in range(int((c/2)**(0.5))+1):
            if ((c - n**2)**(0.5)) % 1 == 0:
                return True
        return False



# Runtime: 317 ms, faster than 58.80% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 13.8 MB, less than 61.87% of Python3 online submissions for Sum of Square Numbers.