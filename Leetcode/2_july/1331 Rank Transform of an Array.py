class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = arr.copy()
        arr2.sort()
        
        d = {}
        rank = 1
        
        for item in arr2:
            if item not in d:
                d[item] = rank
                rank += 1
        
        # print(arr)
        # print(arr2)
        return [d[item] for item in arr ]



# Runtime: 575 ms, faster than 41.28% of Python3 online submissions for Rank Transform of an Array.
# Memory Usage: 30.9 MB, less than 79.47% of Python3 online submissions for Rank Transform of an Array.