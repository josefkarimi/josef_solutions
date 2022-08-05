class Solution:
    def maxProfit(self, prices ):#:List[int]) -> int:
        best = 0
        prices = self.slicing(prices)

        if len(prices) == 0:
            return 0
        else:
            m = prices.index(min(prices))
            M = prices.index(max(prices))
            if M > m :
                return prices[M] - prices[m]
            elif M == m:
                return 0
            else:
                return max(Solution.maxProfit(self,prices[0:M+1]),Solution.maxProfit(self,prices[m:]))
            
    
    
    def slicing(self,mylist):
        start = 0
        end = len(mylist)
        while True:
            try:
                if mylist[start+1] < mylist[start]:
                    start += 1
                else:
                    break
            except:
                break
        while True:
            try:
                if mylist[end-2] > mylist[end-1]:
                    end -= 1
                else:
                    break
            except:
                break
        return mylist[start:end]

        
# print(Solution.maxProfit(Solution,[7,6,4,3,1]))
# print(Solution.maxProfit(Solution,[7,6,4,5,3,1]))
# print(Solution.maxProfit(Solution,[7,1,5,3,6,4]))

# Runtime: 1400 ms, faster than 67.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 38.44% of Python3 online submissions for Best Time to Buy and Sell Stock.