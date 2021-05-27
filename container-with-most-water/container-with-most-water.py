class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        
        left,right = 0,length-1
        maxArea = float('-inf')
        while left <= right:
            maxArea = max(maxArea,min(height[right],height[left]) * (right - left))
            
            if height[left] > height[right]:right-=1
            else:left+=1
        
        return maxArea