class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                temp = s[i:j]
                if len(temp)==1:
                    result+=1
                elif temp == temp[::-1] and temp:
                    result+=1
                    
        return (result)
                
        