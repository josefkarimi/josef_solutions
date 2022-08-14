class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def new_string(s):
            tmp = ""
            for letter in s: 
                if letter == "#":
                    if len(tmp) != 0:
                        tmp = tmp[:len(tmp)-1] 
                        pass
                else :
                    tmp += letter
            return tmp
                    
            
        ss = new_string(s)
        tt = new_string(t)
        
        return ss == tt        
        
                
        

solution = Solution()
# solution.backspaceCompare("xywrrmp","xywrrm#p")
print(solution.backspaceCompare("ab#c","ad#c"))

