class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        for i in range(length):
            j = (abs(nums[i])-1)
            if nums[j] < 0:
                continue
            else:
                nums[j] = nums[j]*(-1)
        print(nums)
        res = []
        
        for i in range(1,length+1):
            if nums[i-1] > 0:
                res.append(i)
        
        return res