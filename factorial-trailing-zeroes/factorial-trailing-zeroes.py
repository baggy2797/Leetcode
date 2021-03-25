class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(5,n+1,5):
            temp = 5
            while i% temp == 0:
                count = count + 1
                temp = temp * 5
                
        return count
        
        
        