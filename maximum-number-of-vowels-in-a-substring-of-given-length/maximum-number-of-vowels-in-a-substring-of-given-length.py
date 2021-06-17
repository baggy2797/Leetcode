class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelCount = count = 0
        j = k-1
        vowels = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowels:
                vowelCount += 1
        count = vowelCount
        for i in range(1, len(s)-(k-1)):
            j+=1
            if s[j] in vowels:
                count += 1 
            if s[i-1] in vowels:
                count -= 1 
            if count > vowelCount:
                vowelCount = count
        return vowelCount