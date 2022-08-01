class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numss = set(nums)
        for item in numss:
            if nums.count(item) == 1:
                return item

# Runtime: 5925 ms, faster than 7.83% of Python3 online submissions for Single Number.
# Memory Usage: 17.1 MB, less than 10.15% of Python3 online submissions for Single Number.
# =======================================================================
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 2:
                pass
            else:
                return i

# Runtime: 9519 ms
# Memory Usage: 16.6 MB
# =======================================================================  

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for item in nums:
            if nums.count(item) == 1:
                return item

# 60 / 61 test cases passed.
# 	Status: Time Limit Exceeded      