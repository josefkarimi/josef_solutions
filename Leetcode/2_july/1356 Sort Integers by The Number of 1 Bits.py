class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def count_of_one(n):
            n = bin(n)
            yeks = n.count("1")
            return yeks
        
        return sorted(arr, key = count_of_one )



# Runtime: 135 ms, faster than 25.65% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# Memory Usage: 14 MB, less than 95.46% of Python3 online submissions for Sort Integers by The Number of 1 Bits.