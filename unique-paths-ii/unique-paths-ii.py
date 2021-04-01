class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:return 0
        if obstacleGrid[m-1][n-1] == 1:return 0
        
        dp = [[0 for _ in range(n)]for _ in range(m)]
        
        dp[0][0] = 1
        
        for row in range(1,m):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row-1][0]
        
        for col in range(1,n):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col-1]
            
        for row in range(1,m):
            for col in range(1,n):    
                if obstacleGrid[row][col]==0:
                    dp[row][col] = dp[row-1][col]+dp[row][col-1]
                else:
                    dp[row][col] = 0
            
        return dp[m-1][n-1]
