class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1
                
        
                
                    
        