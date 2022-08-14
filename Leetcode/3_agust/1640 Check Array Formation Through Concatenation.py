class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for ls in pieces:
            if len(ls) == 1:
                try:
                    arr.index(ls[0])
                except:
                    return False
            else:
                for n in range(len(ls)-1):
                    try:
                        if arr.index(ls[n]) +1 != arr.index(ls[n+1]):
                            return False
                    except:
                        return False
        return True



# Runtime: 45 ms, faster than 91.20% of Python3 online submissions for Check Array Formation Through Concatenation.
# Memory Usage: 13.8 MB, less than 98.56% of Python3 online submissions for Check Array Formation Through Concatenation.