class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 0
        ans = 0
        while ans != k:
            n += 1
            if n in arr:
                pass
            else:
                ans += 1
        return n



# Runtime: 294 ms, faster than 6.38% of Python3 online submissions for Kth Missing Positive Number.
