class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count+=1
                if random.randint(0,count-1) == 0:
                    idx = i
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)