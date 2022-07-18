class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


# Runtime: 375 ms, faster than 45.05% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 97.45% of Python3 online submissions for Binary Search.