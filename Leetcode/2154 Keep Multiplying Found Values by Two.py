class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original



# Runtime: 83 ms, faster than 70.09% of Python3 online submissions for Keep Multiplying Found Values by Two.
# Memory Usage: 14 MB, less than 87.14% of Python3 online submissions for Keep Multiplying Found Values by Two.