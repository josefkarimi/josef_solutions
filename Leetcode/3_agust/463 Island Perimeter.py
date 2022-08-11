class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 :
                    pass 
                else :
                    for (r,c) in [(-1,0),(0,-1),(1,0),(0,1)]:
                        if i+r < 0 or j+c < 0 or i+r >= len(grid) or j+c >= len(grid[0]):
                            ans += 1
                        else:
                            if grid[i+r][j+c] == 0:
                                ans += 1
        return ans 



# Runtime: 769 ms, faster than 62.64% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14.2 MB, less than 71.37% of Python3 online submissions for Island Perimeter.