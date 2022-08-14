class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for op in ops:
            if op == "C":
                ans.pop()
            elif op == "D":
                ans.append(2*ans[len(ans)-1])
            elif op == "+":
                ans.append(ans[len(ans)-1]+ans[len(ans)-2])
            else:
                ans.append(int(op))
        return sum(ans)



#         Runtime: 47 ms, faster than 85.51% of Python3 online submissions for Baseball Game.
# Memory Usage: 14.1 MB, less than 75.54% of Python3 online submissions for Baseball Game.