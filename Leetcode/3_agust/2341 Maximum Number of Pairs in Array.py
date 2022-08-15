from collections import Counter 
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        ans = [0, 0]
        # print(n)
        for item in n:
            ans[0] += n[item]//2
            ans[1] += n[item]%2
        return ans 