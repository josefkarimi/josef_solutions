class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ans = -1 
        for n in range(len(nums)+1):
            c = 0
            for number in nums:
                if number >= n:
                    c += 1
                    if c > n :
                        break
            if c == n:
                return n
        return -1



# Runtime: 40 ms, faster than 89.65% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
# Memory Usage: 13.8 MB, less than 62.52% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.