class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #frequency = Counter(s)
        # print(frequency)
        #seen = set()
        new = ""
        i = 0
        #l = r = 0
        maxLength = 0
    
        for i in s:
            if i not in new:
                new += i
            else:
                maxLength = max(maxLength, len(new))
                idx = new.index(i)
                # print(new[idx+1:],i)
                new = new[idx+1:] + i
                
        maxLength = max(maxLength, len(new))
        
        return maxLength
        
        