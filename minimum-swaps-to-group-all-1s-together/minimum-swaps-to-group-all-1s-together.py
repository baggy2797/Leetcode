class Solution:
    def minSwaps(self, data: List[int]) -> int:
        length = len(data)
        windowSize = sum(data)
        CountOnes = 0
        swaps = 0
        left,right = 0,0
        while right < length:
            CountOnes+= data[right]
            right+=1
            
            if right - left > windowSize:
                CountOnes-= data[left]
                left+=1
            swaps = max(swaps,CountOnes)
        
        return windowSize - swaps
        