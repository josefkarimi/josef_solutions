class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        while "IV" in s:
            ans += 4
            s = s.replace("IV", "",1)
        while "IX" in s:
            ans += 9
            s = s.replace("IX", "",1)
        while "XL" in s:
            ans += 40
            s = s.replace("XL", "",1)
        while "XC" in s:
            ans += 90
            s = s.replace("XC", "",1)
        while "CD" in s:
            ans += 400
            s = s.replace("CD", "",1)
        while "CM" in s:
            ans += 900
            s = s.replace("CM", "",1)
        for l in s:
            if l == "I":
                ans += 1
            elif l == "V":
                ans += 5
            elif l == "X":
                ans += 10
            elif l == "L":
                ans += 50
            elif l == "C":
                ans += 100
            elif l == "D":
                ans += 500
            elif l == "M":
                ans += 1000
        return ans



# Runtime: 113 ms, faster than 7.37% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14 MB, less than 31.19% of Python3 online submissions for Roman to Integer.




class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)):
            if i + 1 <len(s) and roman[s[i]]<roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
            return result