class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti={}
        for i in nums:
            if i not in dicti:
                dicti[i] = 1
            else:
                dicti[i] = dicti[i]+1
        print(dicti)
        for i in dicti:
            if dicti[i] == 1:
                return i
            