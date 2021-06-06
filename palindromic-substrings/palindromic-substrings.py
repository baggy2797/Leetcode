class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
            a b c
        a   1 0 0
        b   0 1 0
        c   0 0 1
        '''
        length = len(s)
        # rows,cols = length,length
        dp = [[0 for _ in range(length)] for _ in range(length)]
        ans= 0
        for i in range(length):
            dp[i][i] = 1
            ans+=1
            
        for i in range(length-1):
            # print(s[i],s[i+1])
            if s[i] == s[i+1]:
                dp[i][i+1] =1
                ans+=1
                
        for Len in range(3,length+1):
            for i in range(length-Len+1):
                j = i + Len-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    ans+=1
        return ans