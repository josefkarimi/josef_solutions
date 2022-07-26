class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def oneeqzero(s):
            if s.count("1") != s.count("0"):
                return False
            elif s[0:len(s)//2].count("1") == (len(s)//2):
                return True
            elif s[0:len(s)//2].count("0") == (len(s)//2):
                return True
            else :
                return False 
        
        # ans = []
        ans = 0
        for start in range(len(s)-1):
            for end in range(start+1, len(s),2):
                stemp = s[start:end+1]
                # print(stemp)
                if oneeqzero(stemp):
                    # ans.append(stemp)
                    ans += 1
        return ans