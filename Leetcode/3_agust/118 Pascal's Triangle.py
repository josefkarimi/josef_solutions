class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        for row in range(2, numRows):
            rowtemp = []
            for i in range(row+1):
                # print("row is: ", row, "i is: ", i)
                if i == 0:
                    # print("i == 0")
                    rowtemp.append(1)
                elif i == row :
                    # print("i == row ")
                    rowtemp.append(1)
                else:
                    # print("else")
                    rowtemp.append(ans[row-1][i-1]+ans[row-1][i])
            ans.append(rowtemp)
        return ans[0:numRows]



# Runtime: 44 ms, faster than 61.12% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 65.76% of Python3 online submissions for Pascal's Triangle.