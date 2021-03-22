class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.dfsofIslands(grid,i,j)
                    maximum = max(maximum,self.count)
                    self.count = 0
        
        return maximum
    
    
    
    def dfsofIslands(self,grid,x,y)->int:
        if x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y]!=1:
            return
        else:
            
            self.count = self.count +1
            grid[x][y] = 0
            self.dfsofIslands(grid,x+1,y)
            self.dfsofIslands(grid,x-1,y)
            self.dfsofIslands(grid,x,y+1)
            self.dfsofIslands(grid,x,y-1)
        