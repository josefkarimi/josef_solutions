class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ml = []
        for row in range(len(mat)):
            ml.append((sum(mat[row]), row))
        print(ml)
        ml.sort()
        print(ml)
        return [ml[n][1] for n in range(k)]



# Runtime: 157 ms, faster than 60.37% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.1 MB, less than 99.16% of Python3 online submissions for The K Weakest Rows in a Matrix.