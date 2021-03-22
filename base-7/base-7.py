class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        sign = 0
        if num < 0:
            sign = 1
            num = (-1)*num
        
        
        factor = 7
        new = ""
        while num > 0:
            temp  = num % 7
            new = new + str(temp)
            num = num//7
        
        if sign == 1:
            return "-"+new[::-1]
        return new[::-1]
                
            
        