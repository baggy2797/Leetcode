class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp = 0
        
        for char in s:
            temp^=ord(char)
        
        for char in t:
            temp^=ord(char)
            
        return chr(temp)