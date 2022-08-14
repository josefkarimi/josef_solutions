from collections import Counter

i =  (("1807", "7810"),("1123", "0111"))


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # g = Counter(guess)
        # s = Counter(secret)
        # cows = dict()
        # bulls = 0
        # for num in s.keys():
        #     if num in g.keys():
        #         cows[num] = min(s[num],g[num])
        #         print(cows)


        numb = ["0","1","2","3","4","5","6","7","8","9"]
        gdic = {n:0 for n in numb}
        sdic = {n:0 for n in numb}
        cows = 0
        bulls = 0 
        for i in gdic.keys():
            gdic[i] = self.find_indices(guess,i)
            sdic[i] = self.find_indices(secret,i)
            inter = len(sdic[i].intersection(gdic[i]))
            bulls += inter
            cows += min(len(gdic[i]),len(sdic[i])) - inter

        return f"{bulls}A{cows}B"




    def find_indices(self, reshte, harf):
        indices = set()
        tmpreshte = reshte[:]
        for i in range(Counter(reshte)[harf]):
            indices.add(tmpreshte.find(harf))
            tmpreshte = tmpreshte.replace(harf," ",1)
            # print(tmpreshte, indices)
        return indices

solution = Solution()
for x in i:
    print(solution.getHint(x[0],x[1]))
    print("-"*10)
    # solution.find_indices(x[0],"1")





# Runtime: 193 ms, faster than 5.10% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 14.2 MB, less than 6.03% of Python3 online submissions for Bulls and Cows.