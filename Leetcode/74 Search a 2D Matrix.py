class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        start = 0
        end = len(matrix)
        
        while start != end and start != end -1 :
            row = (start + end)//2
            if matrix[row][0] > target:
                end = row
            else:
                    start = row
            print(start, end, row)   

        try:
            matrix[start].index(target)
            return True
        except:
            return False



# Runtime: 87 ms, faster than 17.69% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 42.69% of Python3 online submissions for Search a 2D Matrix.