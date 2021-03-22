class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        val = ""
        for i in range(len(s)):
            if s[i] not in dict1: 
                if t[i] not in val:
                    dict1[s[i]] = t[i]
                    val += t[i]
                else:
                    return False
            else: 
                if dict1[s[i]] != t[i]:
                    return False
        return True
            
        
            
        
        
