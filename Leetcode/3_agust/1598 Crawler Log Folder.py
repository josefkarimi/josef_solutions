class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if ans == 0:
                    continue
                else:
                    ans -= 1
            else:
                ans += 1
                    
        return ans 



# Runtime: 83 ms, faster than 31.97% of Python3 online submissions for Crawler Log Folder.
# Memory Usage: 14 MB, less than 87.04% of Python3 online submissions for Crawler Log Folder.