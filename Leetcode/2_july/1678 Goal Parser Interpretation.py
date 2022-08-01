class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for ind in range(len(command)):
            if command[ind] == "G":
                ans += "G"
            elif command[ind] == "(" :
                if command[ind+1] == ")":
                    ans += "o"
                else :
                    ans += "al"
            else :
                pass
        return ans



# Runtime: 34 ms, faster than 86.12% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 13.9 MB, less than 10.02% of Python3 online submissions for Goal Parser Interpretation.