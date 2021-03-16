class Solution:
    def decodeString(self, s: str) -> str:
        i,length = 0,len(s)
        stack = []
        tok,number = "",0
        while i<length:
            
            if s[i] == "[":
                stack.append((tok,number))
                tok = ""
                number = 0
            elif s[i] == "]":
                prev,num = stack.pop()
                tok = prev + tok * num
            elif s[i].isdigit():
                number = number*10 + int(s[i])
            else:
                tok = tok+s[i]
            
            i = i+1
        
        return tok
                
                
        