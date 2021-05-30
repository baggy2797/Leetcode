class Solution:
    def trap(self, height: List[int]) -> int:
        #maximum to the left
        #maximum to the right
        #minus me
        leftMax = rightMax = 0
        ans = 0
        length = len(height)
        for i in range(length):
            leftMax = max(height[:i+1])
            rightMax = max(height[i:])
            
            ans+= min(leftMax,rightMax) - height[i]
        
        return (ans)