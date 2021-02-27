class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 , len(height)-1
        final = 0
        maxl = maxr = 0

        while l<r:
            if height[l] < height[r]:
                #Find the maximum to its left and to its right and subtract itself from min of both the maximums
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    # add the result to final_result
                    final = final + maxl - height[l]
                l = l+1
            else:
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    final = final + maxr - height[r]
                r = r-1
        return final