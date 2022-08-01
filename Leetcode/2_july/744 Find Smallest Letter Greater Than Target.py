class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        o = ord(target)
        for i in letters:
            if ord(i) > o:
                return i
        return letters[0]


# Runtime: 217 ms, faster than 14.96% of Python3 online submissions for Find Smallest Letter Greater Than Target.
# Memory Usage: 14.5 MB, less than 21.62% of Python3 online submissions for Find Smallest Letter Greater Than Target.