class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ind = 0
        ans = s[0]
        
        while ind < n:
            left = ind - 1
            right = ind +1
            
            while right < n and s[ind] == s[right]:
                if len(ans) < right-ind+1:
                    ans = s[ind:right+1]
                
                right = right+1
            
            while left>=0 and right <n and s[left] == s[right]:
                if len(ans) < right - left+1:
                    ans = s[left:right+1]
                left = left-1
                right = right+1
            
            ind = ind+1
        
        return ans
                
                    
       
                
                
                
                
                
        
        
        
            