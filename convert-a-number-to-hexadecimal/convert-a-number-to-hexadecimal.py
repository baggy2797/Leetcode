class Solution:
    def toHex(self, num: int) -> str:
        
        
        if num < 0:
            num += 2**32

        hexadecimal = "0123456789abcdef"
        hex_num = ""
        while num:
            hex_num = hexadecimal[num % 16] + hex_num
            num //= 16
        return hex_num if hex_num else "0"
            
        