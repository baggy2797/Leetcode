class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # if len(matrix) == 1:
        #     if matrix[0][0] =="0":
        #         return 0
        if not matrix:
            return 0
        
        dp = [[0]* (len(matrix[0])+1) for _ in range(len(matrix)+1) ]
        
        
        maxi = 0
        for row in range(1,len(matrix)+1):
            for col in range(1,len(matrix[0])+1):
                if matrix[row-1][col-1] == '1':
                    dp[row][col] = min(dp[row][col-1],dp[row-1][col-1],dp[row-1][col]) + 1
                    maxi = max(maxi,dp[row][col])
        # print(dp)
        return maxi*maxi
        