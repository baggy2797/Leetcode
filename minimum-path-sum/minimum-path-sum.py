class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for row in range(m):
            for col in range(n):
                if row==0 and col ==0:
                    continue
                elif row ==0 and col!=0:
                    grid[row][col] = grid[row][col]+grid[row][col-1]
                elif row!=0 and col==0:
                    grid[row][col] = grid[row][col]+grid[row-1][col]
                else:
                    grid[row][col] = grid[row][col] + min(grid[row][col-1],grid[row-1][col])
        
        return grid[row][col]
                
                