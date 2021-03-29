class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)+1
        
        total,j = 0,0
        
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                new = i-j + 1
                if length > new:
                    length = new
                total -=nums[j]
                j+=1
        return 0 if length > len(nums) else length
        # # print(length)
        # for i in range(len(nums)+1):
        #     for j in range(i+1,len(nums)+1):
        #         # print(target,sum(nums[i:j]))
        #         if sum(nums[i:j]) >= target  and len(nums[i:j]) < length :
        #                 length = len(nums[i:j])
        # if length == sys.maxsize:
        #     return 0
        # return (length)
            
            
            
       
        