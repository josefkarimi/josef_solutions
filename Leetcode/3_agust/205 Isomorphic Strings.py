class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        z = dict(zip(s,t))
        ans = ''
        for i in range(len(s)):
            ans += z.get(s[i])
        if len(set(z.values())) != len(z):
            return False
        return ans == t