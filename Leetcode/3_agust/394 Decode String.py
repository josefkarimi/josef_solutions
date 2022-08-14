class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i]!= ']':
                stack.append(s[i])
                
            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop()+string
                stack.pop()
                
                k =''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * string)
                
        return ''.join(stack)




#         Runtime: 33 ms, faster than 89.13% of Python3 online submissions for Decode String.
# Memory Usage: 13.8 MB, less than 71.86% of Python3 online submissions for Decode String.