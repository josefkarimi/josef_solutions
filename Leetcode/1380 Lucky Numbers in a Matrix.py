class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        
        mins = set()
        for i in range(m):
            mins.add(min(matrix[i]))
        
        maxs = set()
        for j in range(n):
            maxs.add(max(list(zip(*matrix))[j]))
            
        for item in mins:
            if item in maxs:
                ans.append(item)
        return ans



# Runtime: 253 ms, faster than 25.79% of Python3 online submissions for Lucky Numbers in a Matrix.
# Memory Usage: 14.3 MB, less than 31.16% of Python3 online submissions for Lucky Numbers in a Matrix.