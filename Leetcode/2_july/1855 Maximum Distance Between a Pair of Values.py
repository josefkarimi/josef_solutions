# class Solution:
#     def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
#         def isvalid(i, j):
#             if nums1[i] <= nums2[j] :
#                 return True
#             else:
#                 return False
            
#         def dist(i, j):
#             return abs(i - j)
#         ans = 0
#         for i in range(len(nums1)):
#             for j in range(i, len(nums2)):
#                 if isvalid(i, j) and dist(i, j) > ans:
#                     ans = dist(i,j)
#                     print(i,j)
#         return ans 
                    
    
class Solution:
    def maxDistance(self, n1: List[int], n2: List[int]) -> int:
        i = j = res = 0
        while i < len(n1) and j < len(n2):
            if n1[i] > n2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res