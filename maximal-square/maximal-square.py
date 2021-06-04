class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        maxSqlen = 0
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = 1 + min(dp[row-1][col],dp[row-1][col-1],dp[row][col-1])
                    maxSqlen = max(maxSqlen,dp[row][col])
        return maxSqlen * maxSqlen