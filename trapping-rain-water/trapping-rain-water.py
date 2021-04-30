class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        Area = 0
        leftMax = rightMax = 0
        left,right = 0,length-1
        
        while left < right:
            if height[left] < height[right]:
                if height[left]>leftMax:
                    leftMax = height[left]
                else:
                    Area += leftMax - height[left]
                left+=1
                
            else:
                if height[right] > rightMax:                
                    rightMax = height[right]
                else:
                    Area+= rightMax - height[right]
                right-=1
        return Area
                
                