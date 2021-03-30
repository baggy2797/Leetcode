class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        length = 0
        chars.append("\n")
        print(chars)
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                count+=1
                continue
            chars[length] = chars[i-1]
            length+=1
    
            if count == 1:
                continue
            for n in str(count):
                chars[length] = n
                length+=1
            count = 1
            print(chars)
            
        return (length)
            

        
        
        
        