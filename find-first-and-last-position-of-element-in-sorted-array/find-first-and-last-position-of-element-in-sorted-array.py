class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0: return [-1,-1]
        
        def searchLow(nums,target):
            high,low = 0, length-1
            while high<= low:
                mid = (low+high)//2
                
                if nums[mid] >= target:
                    low = mid - 1
                else:
                    high = mid + 1
            return high
        
        def searchHigh(nums,target):
            high,low = 0, length-1
            while high<= low:
                mid = (low+high)//2
                
                if nums[mid] > target:
                    low = mid - 1
                else:
                    high = mid + 1
            return low
        
        start = searchLow(nums,target)
        end = searchHigh(nums,target)
        
        if 0<=start<length and start <= end and nums[start] == target:
            return [start,end]
        else:
            return [-1,-1]