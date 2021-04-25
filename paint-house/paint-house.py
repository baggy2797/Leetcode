class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rows,cols = len(costs),len(costs[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # print(dp,costs)
        
        for j in range(cols):
            dp[0][j] = costs[0][j]
        
        for i in range(1,rows):
            dp[i][0] = costs[i][0] + min(dp[i-1][1],dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0],dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0],dp[i-1][1])
        
        return min(dp[-1])
                