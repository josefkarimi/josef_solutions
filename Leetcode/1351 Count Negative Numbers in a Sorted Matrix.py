class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0 :
                    ans += len(grid[0]) - j
                    break
        return ans



# Runtime: 264 ms, faster than 8.43% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15 MB, less than 77.80% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.