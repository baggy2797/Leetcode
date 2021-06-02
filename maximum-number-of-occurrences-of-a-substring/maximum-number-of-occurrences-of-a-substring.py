class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        length = len(s)
        windowSize = minSize
        freq = {}
        
        for i in range(length-minSize+1):
            # print(s[i:i+windowSize])
            temp = s[i:i+windowSize]
            if len(set(temp)) <= maxLetters:
                freq[temp] =freq.get(temp,0)+1
        
        return max(freq.values()) if freq else 0