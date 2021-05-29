class Solution:
    def binaryGap(self, n: int) -> int:
        temp = bin(n)[2:]
        print(temp)
        last = None
        minimumDistance = 0
        for i in range(32):
            if (n>>i)& 1:
                if last is not None:
                    minimumDistance = max(minimumDistance,i-last)
                
                last = i
        return minimumDistance
            
            