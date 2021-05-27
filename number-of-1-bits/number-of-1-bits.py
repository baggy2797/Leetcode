class Solution:
    def hammingWeight(self, n: int) -> int:
        summ = 0
        while n!=0:
            summ+=1
            n &= (n-1)
        return summ