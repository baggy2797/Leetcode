class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        
        #for characters of length 1: make it 1
        for i in range(len(s)):
            dp[i][i] = 1
            res+=1
            
        # for cubstrings of length 2 : if both characters are equal : make it 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res+=1
        
        # print(dp)
        
        #for characters of length 3 and above: 
        for length in range(3,len(s)+1):
            for i in range(len(s)-length+1):
                j = i + length-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    res+=1
        
        return res
        
        # for length in range(3,len(s)+1):
        #     for i in range(len(s)-length+1):
        #         j = i+ length-1
        #         if dp[i+1][j-1] and s[i]==s[j]:
        #             dp[i][j]=1
        #             res+=1
        # return res
        