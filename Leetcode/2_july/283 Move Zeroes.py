class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1



# Runtime: 175 ms, faster than 91.06% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.6 MB, less than 65.26% of Python3 online submissions for Move Zeroes.