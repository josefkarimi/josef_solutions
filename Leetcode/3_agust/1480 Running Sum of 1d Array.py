class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for item in range(1, len(nums)):
            nums[item] += nums[item-1]
        return nums
            



# Runtime: 57 ms, faster than 65.84% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14 MB, less than 72.77% of Python3 online submissions for Running Sum of 1d Array.