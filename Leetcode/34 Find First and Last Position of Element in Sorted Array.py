class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        try:
            ans[0] = nums.index(target)
            nums.reverse()
            ans[1] =len(nums) -1 - nums.index(target)
        except:
            pass
        return ans 



# Runtime: 120 ms, faster than 59.99% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 50.23% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.