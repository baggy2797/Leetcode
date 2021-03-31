class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i<len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                i = i+2
            else:
                i = i+1
        
        new_length = len(arr)
        del arr[length:new_length]
        
            
        
        