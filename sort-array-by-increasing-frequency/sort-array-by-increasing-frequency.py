class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse = True)
        count = {}
        
        for num in nums:
            count[num] =count.get(num,0)+1
            
        x =[]
        # print(sorted(count.items()))
        count = {i:j for i,j in sorted(count.items(),key=lambda x: x[1])}
        # print(count)
        for i,j in count.items():
            x += [i]*j
        return x
        