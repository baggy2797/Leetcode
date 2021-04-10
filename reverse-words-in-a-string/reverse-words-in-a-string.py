class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        length = len(s)
        result = ""
        new =""
        res = []
        i = 0
        while i < length:
            if s[i]==" ":
                # temp = s[i]
                while s[i]==" ":
                    i+=1
                res.append(new)
                new = ""
                
            else:
                new+=s[i]
                i+=1
        res.append(new)
        
        result = " ".join(r for r in reversed(res))
        return result
            
        
        