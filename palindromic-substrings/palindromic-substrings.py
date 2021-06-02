class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
            a a a
        a   1 3 
        a     2 
        a       3
        '''
        
        """
            a b c
        a   1 1 1
        b     1 1
        c       1
        
        
        """
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        count = 0
        for i in range(length):
            dp[i][i] =1
            count+=1
        
        for i in range(length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                count+=1
        
        for l in range(3,length+1):
            for i in range(length-l+1):
                j = i+l-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] =1
                    count+=1
                    
        return count
        