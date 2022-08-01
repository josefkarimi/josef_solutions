class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = len(arr1)
        for i, item in enumerate(arr1):
            for j ,jtem in enumerate(arr2):
                if abs(item - jtem) <= d :
                    ans -= 1
                    break
                    
        return ans 



# Runtime: 185 ms, faster than 31.50% of Python3 online submissions for Find the Distance Value Between Two Arrays.
# Memory Usage: 14 MB, less than 41.37% of Python3 online submissions for Find the Distance Value Between Two Arrays.