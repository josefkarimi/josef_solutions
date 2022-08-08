class Solution(object):
    def lengthOfLIS(self, nums):
	########   Dp approach having T(n)=O(n^2)
        n=len(nums)
        dp=[1 for x in range(0,n)]
        for i in range (1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)



# Runtime: 7873 ms, faster than 5.08% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.3 MB, less than 47.45% of Python3 online submissions for Longest Increasing Subsequence.