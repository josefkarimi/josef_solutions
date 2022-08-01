class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            s = sum(accounts[i]) 
            if s > max_wealth :
                max_wealth = s
        return max_wealth

# Runtime: 54 ms, faster than 95.84% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.9 MB, less than 32.12% of Python3 online submissions for Richest Customer Wealth.