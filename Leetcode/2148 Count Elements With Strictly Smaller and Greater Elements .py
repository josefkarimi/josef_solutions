class Solution:
    def countElements(self, nums: List[int]) -> int:
        mm = max(nums)
        mn = min(nums)
        if mm == mn :
            return 0 
        else :
            return len(nums) - nums.count(mm) - nums.count(mn)



#             Runtime: 69 ms, faster than 39.17% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .
# Memory Usage: 14 MB, less than 17.27% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .