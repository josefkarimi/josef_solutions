# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         for i in range(len(triangle)-2,-1,-1):
#             for j in range(0,len(triangle[i])):
#                 triangle[i][j] +=  min(triangle[i+1][j],triangle[i+1][j+1])
#         return triangle[0][0]





class Solution:
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-2, -1, -1):
            for item in range(len(triangle[i])):
                triangle[i][item] += min(triangle[i+1][item],triangle[i+1][item+1])
        return triangle[0][0]
            

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))