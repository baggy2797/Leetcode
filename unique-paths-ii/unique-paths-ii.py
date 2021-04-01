class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # dp
        dp = [[0]*cols for _ in range(rows)]
        # assign the value for staring point
        dp[0][0] = 1
        # assign the first col
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r-1][0]
        # assign the first row
        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                else:
                    dp[r][c] = 0
        
        return dp[rows-1][cols-1]
        
        
        
        
#         m,n = len(obstacleGrid),len(obstacleGrid[0])
        
#         if obstacleGrid[0][0] ==1:return 0
#         if obstacleGrid[m-1][n-1] ==1:return 0
        
#         dp = [[0 for _ in range(n)]for _ in range(m)]
            
#         for row in range(m):
#             for col in range(n):
                
#                 if obstacleGrid[row][col] == 0:
#                     if row == 0 and col == 0:
#                         dp[row][col] = 1
                        
#                     elif row == 0 and col!=0:
#                             dp[row][col] = 1
                    
#                     elif row != 0 and col==0:
#                             dp[row][col] = 1
                    
#                     else:
#                         if obstacleGrid[row][col]==0:
#                             dp[row][col] = dp[row-1][col]+dp[row][col-1]
#                         else:
#                             dp[row][col] = 0
                
#                 else:
#                     dp[row][col]=0
#         print(dp)
#         return dp[m-1][n-1]