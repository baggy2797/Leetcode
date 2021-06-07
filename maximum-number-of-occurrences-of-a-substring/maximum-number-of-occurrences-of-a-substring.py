class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        length = len(s)
        freq = {}
        for i in range(length-minSize+1):
            temp = s[i:i+minSize]
            if len(set(temp)) <= maxLetters:
                if temp in freq:
                    freq[temp]+=1
                else:
                    freq[temp] = 1
        return max(freq.values()) if freq else 0
        