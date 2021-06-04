class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)    
        mx = 0
        for num in nums:
            if num-1 not in st:
                tmp = 1
                while num+1 in st:
                    tmp += 1
                    num += 1
                mx = max(mx, tmp)

        return mx   