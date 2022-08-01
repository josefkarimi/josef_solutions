class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lss = list(s)
        lst = list(t)
        lss.sort()
        lst.sort()
        ind = 0
        while ind < len(lss) and lss[ind] == lst[ind]:
            # print(ind)
            ind += 1
        return lst[ind]


# Runtime: 71 ms, faster than 19.94% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.8 MB, less than 75.54% of Python3 online submissions for Find the Difference.