class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        freq = Counter(s)
        print(freq)
        
        res = 0
        foundOdd = False
        for value in freq.values():
            if value % 2 == 0:
               res += value
            else:
                foundOdd = True
                res+=value-1
        return res+1 if foundOdd else res 