class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if d != arr[i+1] - arr[i]:
                return False
        else:
            return True

# Runtime: 64 ms, faster than 46.35% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# Memory Usage: 14.1 MB, less than 28.69% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
