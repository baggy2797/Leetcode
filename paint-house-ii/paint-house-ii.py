class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        cols = len(costs[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for col in range(cols):
            dp[0][col] = costs[0][col]
        
        for row in range(1,rows):
            for col in range(cols):
                
                dp[row][col] = costs[row][col] + min(dp[row-1][:col]+dp[row-1][col+1:])
        
        return(min(dp[-1]))
        
        
        
        
        
        
        
        
        
        
        
        
        
#         rows,cols = len(costs),len(costs[0])
#         # dp = [0]*(rows+1)
#         globalMinimum = float("inf")
#         globalColNeglect = 0 
#         cost = 0
#         for col in range(cols):
#             if globalMinimum > costs[0][col]:
#                 globalMinimum = costs[0][col]
#                 globalColNeglect = col
#         print(globalMinimum ,globalColNeglect)
#         cost = globalMinimum
        
#         for row in range(1,rows):
#             # print(row)
#             minimum = float("inf")
#             colNeglect = 0
#             for col in range(cols):
#                 if col < globalColNeglect or col > globalColNeglect:
#                     if minimum > costs[row][col]:
#                         minimum = costs[row][col]
#                         colNeglect = col
#                 else:
#                     continue
                        
#             globalColNeglect = colNeglect
#             globalMinimum = minimum
#             cost += globalMinimum   
#             print(globalMinimum ,globalColNeglect)
#             # print(cost)
#         return(cost)
        