class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k ==1:
            return 1
        if k>n:
            return -1
        
        res = [1]
        
        for i in range(2,n+1):
            if n%i == 0:
                res.append(i)
        
        if len(res)<k:
            return -1
        return res[k-1]