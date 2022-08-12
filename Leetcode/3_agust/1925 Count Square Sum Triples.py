class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n-1):
            for j in range(i+1,n):
                sqr = i**2+j**2
                if sqrt(sqr) %1 == 0 and sqr <= n**2:
                    count += 2
        return count



# Runtime: 512 ms, faster than 59.33% of Python3 online submissions for Count Square Sum Triples.
# Memory Usage: 13.8 MB, less than 96.70% of Python3 online submissions for Count Square Sum Triples.