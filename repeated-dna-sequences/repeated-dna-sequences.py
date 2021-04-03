class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        output = set()
        seen = set()
        for i in range(length-10+1):
            tmp = s[i:i+10]
            if tmp in seen:
                output.add(s[i:i+10])            
            seen.add(s[i:i+10])
                    
        return output