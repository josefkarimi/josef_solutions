class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c  = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a+b+c
            # print("a:",a,"b:",b,"c:",c)
        return a
            



# Runtime: 36 ms, faster than 81.20% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 11.97% of Python3 online submissions for N-th Tribonacci Number.


s = Solution()
print(s.tribonacci(234))