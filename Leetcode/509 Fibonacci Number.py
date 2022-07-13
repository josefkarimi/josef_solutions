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

# Runtime: 22 ms
# Memory Usage: 13.8 MB                         


# I found a better Solution

class Solution:
    def fib(self, n: int) -> int:
        def add_fib(arr):
            arr.append(arr[len(arr)-1]+arr[len(arr)-2])
        
        myfib = [0, 1]
        for _ in range(n):
            add_fib(myfib)
        
        return myfib[n]
            
# Runtime: 68 ms, faster than 29.94% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 95.42% of Python3 online submissions for Fibonacci Number.