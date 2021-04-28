class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        summOfA = sum(A)
        length = len(A)
        for i in range(1,length):
            if A[i] <= A[i-1]:
                A[i] = max(A[i],A[i-1]+1)
        summOfAPost = sum(A)
        
        return summOfAPost - summOfA
                
        
        
        
        
        
            