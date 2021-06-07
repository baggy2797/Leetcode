class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        frequency = {}
        left =0 
        longest = 0
        
        for right,char in enumerate(s):
            frequency[char] =frequency.get(char,0)+1
            
            while len(frequency) > k:
                # temp = s[left]
                frequency[s[left]]-=1
                if frequency[s[left]] == 0:
                    del frequency[s[left]]
                left+=1
            
            size = right-left+1
            longest = max(longest,size)
            
        return longest
        