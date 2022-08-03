class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for letter in s:
            # print(letter)
            try: 
                ind = t.index(letter) +1
                t = t[ind:]   
            except:
                return False
            # finally:
            #     print(t)
        return True