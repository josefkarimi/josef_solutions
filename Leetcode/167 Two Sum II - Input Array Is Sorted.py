class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target: return (l + 1,  r + 1)
            if numbers[l] + numbers[r] > target: r -= 1
            else: l += 1




# Runtime: 224 ms, faster than 35.49% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.9 MB, less than 41.23% of Python3 online submissions for Two Sum II - Input Array Is Sorted.