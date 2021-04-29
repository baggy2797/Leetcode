class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        length = len(height)
        left,right = 0, length-1
        
        while left < right:
            area = max(area, min(height[left],height[right]) *(right-left)   )
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return area