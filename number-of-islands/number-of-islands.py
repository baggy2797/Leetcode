class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # self.visited = [[False]* len(grid[0]) for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" :
                # and self.visited[i][j] == False:
                    count = count + 1
                    self.findIslands(i,j,grid)
        print(grid)
        return count
        
    def findIslands(self,x,y,grid):
        if x<0 or y<0 or x==len(grid) or y ==len(grid[0]) or grid[x][y]!='1':
        
            return
        else:
            # self.visited[x][y] = True
            grid[x][y] = '0'
            self.findIslands(x+1,y,grid)
            self.findIslands(x-1,y,grid)
            self.findIslands(x,y+1,grid)
            self.findIslands(x,y-1,grid) 
        