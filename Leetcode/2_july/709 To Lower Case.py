# class Solution:
#     def toLowerCase(self, s: str) -> str:
#         return s.lower()


# Runtime: 43 ms, faster than 61.31% of Python3 online submissions for To Lower Case.
# Memory Usage: 13.9 MB, less than 49.73% of Python3 online submissions for To Lower Case.

class Solution:

    def toLowerCase(self, s: str) -> str: 
        from string import ascii_letters

        nstr = ""
        for item in s:
            try:
                ind = ascii_letters.index(item)
                if ind > 25:
                    nstr += ascii_letters[ind-26]
                else:
                    nstr += ascii_letters[ind]
            except:
                nstr += item
        return nstr 


# Runtime: 55 ms, faster than 27.10% of Python3 online submissions for To Lower Case.
# Memory Usage: 13.8 MB, less than 49.73% of Python3 online submissions for To Lower Case.
