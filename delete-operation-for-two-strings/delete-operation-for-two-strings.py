class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word1)+1) for row in range(len(word2)+1)]
        
        for i in range(1, len(word2)+1):
            
            for j in range(1, len(word1)+1):
                
                if word1[j-1] == word2[i-1]:
                    
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return len(word1) + len(word2) - 2*dp[-1][-1]
        
                