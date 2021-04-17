class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s,len_p = len(s),len(p)
        dp = [[0 for i in range(len_s+1)] for j in range(len_p+1)] 
        dp[0][0] = 1
        i=0
        while i<len(p) and p[i]=="*":
            dp[i+1][0]=1
            i+=1
        for i in range(1,len_p+1):
            for j in range(1,len_s+1):
                if p[i-1]==s[j-1] or p[i-1]=="?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1]=="*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = 0
                    
        return dp[len(p)][len(s)]
