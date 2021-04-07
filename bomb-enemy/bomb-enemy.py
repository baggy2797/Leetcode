class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if( not grid ): return 0
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [ [[0,0,0,0] for __ in range(cols)] for _ in range(rows) ]
        res = 0
        
        # left to right
        for i in range(rows):
            runningSum = 0
            for j in range(cols):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][0] = runningSum
        
        # right to left
        for i in range(rows):
            runningSum = 0
            for j in range(cols-1, -1, -1):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][1] = runningSum
        
        # top to bottom
        for j in range(cols):
            runningSum = 0
            for i in range(rows):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][2] = runningSum
        
        # bottom to top
        for j in range(cols):
            runningSum = 0
            for i in range(rows-1, -1, -1):
                if( grid[i][j] == "E" ):
                    runningSum += 1
                elif( grid[i][j] == "W" ):
                    runningSum = 0
                else:
                    dp[i][j][3] = runningSum
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='0':
                    res = max(res,sum(dp[i][j]))
        return res        