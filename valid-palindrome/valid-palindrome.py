class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower().replace(":","").replace(",","").replace(" ","").replace(".","")
        s=re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        return s == s[::-1] 
        