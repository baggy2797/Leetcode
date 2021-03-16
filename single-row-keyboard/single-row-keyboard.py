class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        for i in range(len(word)):
            j = keyboard.index(word[i])
            if i==0:
                result = j
            else:
                result = result + abs(j-keyboard.index(word[i-1]))
        
        return (result)
            