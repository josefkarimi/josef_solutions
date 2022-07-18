# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        temp = n
        start = 1
        end = n 
        while guess(temp) != 0:
            if guess(temp) == -1:
                end = temp
                temp = (start+end)//2
            else:
                start = temp
                temp = (start+end)//2
        return temp
                
        

# Runtime: 29 ms, faster than 94.59% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 13.8 MB, less than 97.29% of Python3 online submissions for Guess Number Higher or Lower.



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while start != end and start != end -1:
            if guess((end+start)//2) == 0:
                return (end+start)//2
            elif guess((end+start)//2) == 1:
                start = (end+start)//2
            elif guess((end+start)//2) == -1:
                end = (end+start)//2
        
        if guess(start) == 0:
            return start
        else:
            return end
        