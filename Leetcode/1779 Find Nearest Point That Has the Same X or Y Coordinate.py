class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def valid_points(x, y, p):
            if p[0] == x or p[1] == y:
                return True
            else:
                return False
        
        def dist(x, y, p):
            return abs(p[0]-x) + abs(p[1]-y)
        
        if [x, y] in points:
            return (points.index([x,y]))
        
        ans = ""
        d = ""
        for i in range(len(points)):
            if valid_points(x, y, points[i]):
                # print(dist(x,y,points[i]),"i is",i, points[i])
                if d:
                    if d > dist(x, y, points[i]):
                        ans = i
                        d = dist(x, y, points[i])
                    
                else:
                    d = dist(x, y, points[i])
                    ans = i
                # print("d is", d,"i is",i, "ans is",ans)
        if ans != "":
            return ans
        else:
            return -1