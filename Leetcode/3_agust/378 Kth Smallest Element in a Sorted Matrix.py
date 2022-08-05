class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_nums = [] #create a list for all numbers in matrix
        for n in range(len(matrix)): 
            all_nums.extend(matrix[n])
            # print(jjj)
        all_nums.sort()
        # print("sorted",jjj)
        return all_nums[k-1]



# Runtime: 190 ms, faster than 94.31% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 18.6 MB, less than 80.82% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.