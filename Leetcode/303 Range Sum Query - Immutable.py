class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)




# Runtime: 1651 ms, faster than 17.22% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.5 MB, less than 84.20% of Python3 online submissions for Range Sum Query - Immutable.