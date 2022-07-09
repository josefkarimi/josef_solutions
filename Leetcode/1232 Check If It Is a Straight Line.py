class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def shib(a, b):
            if a[0] == b[0]:
                return 0 
            elif a[1] == b[1]:
                return "inf"
            return (b[1]-a[1])/(b[0]-a[0])
        
        try:
            m = shib(coordinates[0], coordinates[1])
        except:
            return False
        
        for i in range(1, len(coordinates)-1):
            if m != shib(coordinates[i], coordinates[i+1]):
                return False
        return True