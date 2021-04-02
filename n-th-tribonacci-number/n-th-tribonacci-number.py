class Solution:
    def tribonacci(self, n: int) -> int:
        
        storage = [0]*38
        storage[0] = 0
        storage[1] = 1
        storage[2] = 1
        
        
        def helper(n):
            if n==0:
                return storage[n]
            elif n==1 or n==2:
                return storage[n]
            else:
                if storage[n]!=0:
                    return storage[n]
                else:
                    result = helper(n-3) + helper(n-2) + helper(n-1)
                    storage[n] = result
                    return result
        
        return helper(n)
        
        
            
                