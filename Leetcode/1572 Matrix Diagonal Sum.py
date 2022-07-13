class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)%2 == 0:
            ans = 0
        else :
            ans = -mat[len(mat)//2][len(mat)//2]
        for i in range(len(mat)):
            ans += mat[i][i] + mat[i][len(mat)-1-i]
        return ans
        


# Runtime: 186 ms, faster than 37.65% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14.2 MB, less than 55.10% of Python3 online submissions for Matrix Diagonal Sum.