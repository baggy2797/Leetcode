class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] >0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                low,high = i+1,len(nums)-1

                while low<high:
                    summ = nums[i] + nums[low]+nums[high]
                    if summ <0:
                        low = low+1
                    elif summ > 0:
                        high = high-1
                    else:
                        res.append([nums[i],nums[low],nums[high]])
                        low = low+1
                        high = high-1
                        while low<high and nums[low] == nums[low-1]:
                            low = low+1
        return res
                    
                    
        
        