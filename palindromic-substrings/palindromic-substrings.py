class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1] and temp:
                    result.append(temp)
                    
        return len(result)
                
        