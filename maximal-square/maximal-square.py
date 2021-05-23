class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0: return 0
        cols= len(matrix[0])
        height = 0
        
        dp = [[0 for _ in range(cols+1)]for _ in range(rows+1)]
        
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    height = max(height,dp[i][j])
        return height**2