class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if s == s[::-1]:
            return s
        
        left,right = len(s)-1,len(s)-1
        
        while left <=right and left>=0:
            temp = s[left:right+1]
            temp = temp[::-1]
            # print(temp) 
            new = temp + s
            # print(new)
            if new == new [::-1]:
                return new
            left = left-1
    
        
        