class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def shib(a, b):
            if a == b :
                return "same"
            elif a[0] == b[0]:
                return inf
            elif a[1] == b[1]:
                return 0
            else:
                return (b[1]-a[1])/(b[0]-a[0])
            
        if shib(points[0],points[1]) == shib(points[0],points[2]) or shib(points[0],points[1]) == shib(points[1],points[2]) or shib(points[1],points[2]) == shib(points[0],points[2]):
            return False
        elif shib(points[0],points[1]) == "same" or shib(points[2],points[1]) == "same" or shib(points[0],points[2]) == "same":
            return False
        else:
            return True



# Runtime: 51 ms, faster than 49.07% of Python3 online submissions for Valid Boomerang.
# Memory Usage: 13.9 MB, less than 62.87% of Python3 online submissions for Valid Boomerang.