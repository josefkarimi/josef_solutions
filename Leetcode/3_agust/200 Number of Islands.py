class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = 0
        def isisland(cordinate):
            if grid[cordinate[0]][cordinate[1]] == "0":
                return 0
            else:
                new_lands = [cordinate]
                lands = set()
                while new_lands:
                    if new_lands[0] in lands:
                        new_lands.pop(0)
                    else:
                        lands.add(new_lands[0])
                        for i_add, j_add in [(-1,0), (0,-1), (1,0), (0,1)]:
                            new_i = new_lands[0][0] + i_add
                            new_j = new_lands[0][1] + j_add
                            if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                                pass 
                            else :
                                if grid[new_i][new_j] == "0":
                                    pass
                                else :
                                    new_lands.append((new_i,new_j))
                for cor in lands:
                    grid[cor[0]][cor[1]] = "0"
                return 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                n += isisland((i,j))
                # print("i:",i,"j:",j,"n:",n)
        return n




# Runtime: 563 ms, faster than 32.68% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.1 MB, less than 97.56% of Python3 online submissions for Number of Islands.