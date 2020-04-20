class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #TODO
        m = len(grid[0]) -1
        n = len(grid) -1
        def findmin(s, grid, x,y):
            s += grid[x][y]
            if x == m and y == n:
                return s
            elif x == m:
                return findmin(s,grid,x,y + 1)
            elif y == n:
                return findmin(s,grid,x + 1,y)
            else:
                return min(findmin(s,grid,x+1,y), findmin(s,grid,x,y+1))
            
        return findmin(0,grid,0,0)
                
                
        