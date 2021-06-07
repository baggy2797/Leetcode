class Solution:
    def minSwaps(self, data: List[int]) -> int:
        noOfOnes = sum(data)
        windowSize = noOfOnes
        length = len(data)
        right = 0
        left = 0
        currentOnes = 0
        swaps = 0
        while right < length:
            currentOnes += data[right]
            right+=1
            
            if right - left > windowSize:
                currentOnes-=data[left]
                left+=1
            swaps = max(currentOnes,swaps)
        return windowSize - (swaps) 
            