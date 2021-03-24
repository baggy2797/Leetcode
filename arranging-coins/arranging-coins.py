class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        while n>0:
            if n > count:
                count+=1 
            else:
                return count
            n=n-count
        return count