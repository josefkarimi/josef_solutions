class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(map(int, str(num)))
        evens = sorted(x for x in digits if x % 2 == 0)
        odds = sorted(x for x in digits if x % 2 == 1)
        return ''.join(str(odds.pop() if x%2==1 else evens.pop()) for x in digits)
    



# Runtime: 53 ms, faster than 37.98% of Python3 online submissions for Largest Number After Digit Swaps by Parity.
# Memory Usage: 13.8 MB, less than 98.13% of Python3 online submissions for Largest Number After Digit Swaps by Parity.