class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2 :
            return max(nums[0],nums[1])
        elif len(nums) == 3 :
            return max(nums[0]+nums[2],nums[1])
        else:
            nums[2] += nums[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-2],nums[i-3])
        return max(nums[len(nums)-1],nums[len(nums)-2])


# Runtime: 60 ms, faster than 21.50% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 65.68% of Python3 online submissions for House Robber.