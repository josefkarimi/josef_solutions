class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        now = 1
        b = 1
        bb = 0 
        while now != n:
            x = b + bb 
            bb = b
            b = x
            now += 1
        return b