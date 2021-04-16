class Solution:
    def reverseVowels(self, s: str) -> str:
        left,length,right = 0,len(s),len(s)-1
        s = list(s)
        while left < right:
            if s[left] in {'A','a','e','E','i','I','o','O','u','U'} and s[right] in {'A','a','e','E','i','I','o','O','u','U'} :
                s[left],s[right] = s[right],s[left] 
                left+=1
                right-=1
            elif s[left] not in {'A','a','e','E','i','I','o','O','u','U'}:
                left+=1
            elif s[right] not in {'A','a','e','E','i','I','o','O','u','U'}:
                right-=1
        return "".join(s)
            
        
                
        