class Solution:
    # def __init__(self):
    #     self.cache = {}
    @lru_cache(maxsize = 45)
    def climbStairs(self, n: int) -> int:
        if n == 1 or n ==2 :
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        
            