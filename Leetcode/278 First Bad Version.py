# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start != end and start != end-1:
            if isBadVersion((end + start)//2):
                end = (end + start)//2
                print("end", end)
            else:
                start = (end + start)//2
                print("start", start)
        
        if isBadVersion(start):
            return start
        else:
            return end



# Runtime: 40 ms, faster than 68.06% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.9 MB, less than 60.97% of Python3 online submissions for First Bad Version.