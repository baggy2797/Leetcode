class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []
        for i in range(2**length,2**(length+1)):
            new = bin(i)[3:]
            res.append([nums[j] for j in range(length) if new[j] =='1'])
            
        return res
               
        # res = []
        # for i in range(len(nums)+1):
        #     for j in range(i,len(nums)+1):
        #         if nums[i:j] == []:
        #             if [] not in res:
        #                 res.append(nums[i:j])
        #             else:
        #                 continue
        #         else:
        #             res.append(nums[i:j])
        # return(res)
        