class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return i


# Runtime: 798 ms, faster than 5.19% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 27.2 MB, less than 5.41% of Python3 online submissions for Peak Index in a Mountain Array.
