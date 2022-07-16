class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def create_island(s):
            new_lands = [s]
            lands = set()

            while new_lands:
                if new_lands[0] in lands :
                    new_lands.pop(0)
                else:
                    lands.add(new_lands[0])
                    for n,m in ((new_lands[0][0]+1,new_lands[0][1]),(new_lands[0][0],new_lands[0][1]+1),(new_lands[0][0],new_lands[0][1]-1),(new_lands[0][0]-1,new_lands[0][1])):
                        try:
                            if n >= 0 and m >= 0 and grid[n][m]:
                                new_lands.append((n,m))
                        except IndexError:
                            pass
            for item in lands:
                grid[item[0]][item[1]] = 0
            return len(lands)       
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] :
                    c = max(c, create_island((i,j)))
    
        return c



# Runtime: 209 ms, faster than 56.02% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.4 MB, less than 84.63% of Python3 online submissions for Max Area of Island.