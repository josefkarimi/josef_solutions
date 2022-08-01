class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            mat[i][0] = 1
        for j in range(n):
            mat[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] += mat[i-1][j] + mat[i][j-1]
                
                
                
        return (mat[m-1][n-1])



# Runtime: 40 ms, faster than 76.07% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 73.95% of Python3 online submissions for Unique Paths.