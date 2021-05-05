class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def helper(n, power):
            if n == 0:
                return True
            
            if power < 0 and n != 0:
                return False
            
            if n >= pow(3, power):
                return helper(n - pow(3, power), power - 1)

            elif n < pow(3, power):
                return helper(n, power - 1)
        
        return helper(n, 16)

        
        