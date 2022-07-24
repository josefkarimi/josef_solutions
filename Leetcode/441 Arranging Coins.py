class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = 0
        s = 0
        while s <= n :
            x += 1
            s = x*(x+1)/2
        return x -1



# Runtime: 2326 ms, faster than 5.70% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.7 MB, less than 96.49% of Python3 online submissions for Arranging Coins.