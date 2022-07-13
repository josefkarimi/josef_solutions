class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        
        if n*m != r*c:
            return mat
        
        mylist = []
        
        for i in range(m):
            for j in range(n):
                mylist.append(mat[i][j])
        ans = []
        for i in range(r):
            ans.append(mylist[i*c:i*c+c])
        
        return ans


# Runtime: 155 ms, faster than 37.90% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.6 MB, less than 98.74% of Python3 online submissions for Reshape the Matrix.