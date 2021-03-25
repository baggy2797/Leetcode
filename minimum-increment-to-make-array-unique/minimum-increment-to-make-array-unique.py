class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        
        count = 0
        prev_num = float('-inf')
        
        for curr_num in A:
            if prev_num >= curr_num:
                count += prev_num - curr_num + 1
                prev_num = prev_num + 1
            else:
                prev_num = curr_num
        
        return count
                
        
        