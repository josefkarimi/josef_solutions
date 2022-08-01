class Solution:
    def isHappy(self, n: int) -> bool:
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1 

# Runtime: 58 ms, faster than 38.49% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 13.91% of Python3 online submissions for Happy Number.



class Solution:
    def isHappy(self, n):
        while n > 4:
            n = sum(int(d)**2 for d in str(n))
        return n == 1

# Runtime: 58 ms, faster than 38.49% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 96.79% of Python3 online submissions for Happy Number.