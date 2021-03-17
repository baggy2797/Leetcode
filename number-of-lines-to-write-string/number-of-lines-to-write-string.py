class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l,wi = 1,0
        for char in s:
            w = widths[ord(char)-ord('a')]
            wi = wi + w
            if wi > 100:
                l = l+1
                wi = w
            
        return l,wi
                
            
        