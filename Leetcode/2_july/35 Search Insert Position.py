class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i in nums:
                if i > target:
                    print(i)
                    return nums.index(i)
            return len(nums)



# Runtime: 55 ms, faster than 87.38% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.6 MB, less than 82.82% of Python3 online 

enumerate