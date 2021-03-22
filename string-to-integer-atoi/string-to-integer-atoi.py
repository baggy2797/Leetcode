import re
class Solution:
    def myAtoi(self, str: str) -> int:
        match = re.match(r'^\s*([+-]?\d+)', str)
        return min(max((int(match.group(1)) if match else 0), -2**31), 2**31 - 1)
        
        
       
        
            
        