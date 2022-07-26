class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        beg, end = 0, len(nums) - 1
        
        while beg <= end:
            if nums[beg] % 2 == 0:
                beg += 1
            else:
                nums[beg], nums[end] = nums[end], nums[beg]
                end -= 1
        return nums



# Runtime: 75 ms, faster than 98.59% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 60.28% of Python3 online submissions for Sort Array By Parity.