class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = set(arr)
        # print(table)
        try:
            arr.remove(0)
        except:
            pass
        for item in arr:
            # print(item)

            if item * 2 in table:
                return True
        return False



# Runtime: 54 ms, faster than 95.17% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 13.9 MB, less than 53.83% of Python3 online submissions for Check If N and Its Double Exist.