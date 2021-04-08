class Solution:
    def sortString(self, s: str) -> str:
        seen = sorted(list(set(s)))
        freq = {}
        res = ""
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]]+=1
        
        while(freq):
            for char in seen:
                if char in freq:
                    res += char
                    freq[char] -= 1
                    if freq[char] == 0:
                        del freq[char]
            for char in reversed(seen):
                if char in freq:
                    res += char
                    freq[char] -= 1
                    if freq[char] == 0:
                        del freq[char]
            # print(res)
        return res
        
            
            
            
    
                
                