class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        temp = []
        for i in range(1,n+1):
            if n%i == 0:
                temp.append(i)
        
        if len(temp) >=k : return temp[k-1]
        return -1