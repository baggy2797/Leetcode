class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        rows,cols = len(grid),len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        def dfs(grid,x,y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y]!="1" or visited[x][y] == 1:
                return 
            
            visited[x][y] = 1
            dfs(grid,x+1,y)
            dfs(grid,x-1,y)
            dfs(grid,x,y+1)
            dfs(grid,x,y-1)
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col]==0:
                    dfs(grid,row,col)
                    count+=1
        print(visited)
        return count