class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s:return 0
        if k>=len(s):return len(s)
        if k == 0:return 0
        
        
        length = len(s)
        
        windowSize = 0
        right = 0
        left = 0
        temp = {}
        maxLength = 1
        
        while right < length: 
            if s[right] in temp:
                temp[s[right]]+=1
            else:
                windowSize+=1
                temp[s[right]] = 1
            
            if windowSize<= k:
                maxLength = max(maxLength,right - left + 1)
            
            else:
                if s[left] in temp:
                    temp[s[left]] -= 1
                    if temp[s[left]] == 0:
                        del temp[s[left]]
                        windowSize-=1
                left+=1
            
            right+=1
        
            # print(left,right)
            # print(temp)
        return (maxLength)
                    
        
        