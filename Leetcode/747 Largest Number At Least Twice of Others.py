class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        ans = (nums.index(m), m)
        nums.pop(ans[0])
        m2 = max(nums)
        print(nums,m,m2)
        if m >= m2*2:
            return ans[0]
        else:
            return -1



# Runtime: 57 ms, faster than 44.23% of Python3 online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 13.8 MB, less than 59.38% of Python3 online submissions for Largest Number At Least Twice of Others.