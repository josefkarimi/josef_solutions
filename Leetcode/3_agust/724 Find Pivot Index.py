# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n = 0
#         l = len(nums)
#         while n < l :
#             if sum(nums[0:n]) != sum(nums[n+1:l]):
#                 n += 1
#             elif sum(nums[0:n]) == sum(nums[n+1:l]): 
#                 return n
#         return -1


# 742 / 745 test cases passed.
# 	Status: Time Limit Exceeded
	


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i-1] == sum(nums[i+1:len(nums)]):
                return i
        return -1



# Runtime: 6507 ms, faster than 5.30% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.3 MB, less than 10.87% of Python3 online submissions for Find Pivot Index.