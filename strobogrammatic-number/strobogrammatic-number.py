class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = []
        
        for c in reversed(num):
            if c in {'0','1','8'}:
                rotated.append(c)
            
            elif c == '6':
                rotated.append('9')
            elif c == '9':
                rotated.append('6')
            else:
                return False
            
        rotated = "".join(rotated)
        
        return rotated == num