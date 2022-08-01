class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x == 0:
                return 0
            elif x < 0:
                return -1
            else:
                return 1
        
        
        
        
        if 0 in nums:
            return 0
        else:
            pr = 1
            mylist = map(signFunc, nums)
            for i in mylist:
                pr *= i
        return pr