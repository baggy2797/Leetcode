class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        copy = grid
        res = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        left_to_right,bottom_to_top = [],[]
        
        for row in range(len(grid)):
            left_to_right.append(max(grid[row]))
        
        for row in range(len(grid)):
            temp = 0
            for col in range(len(grid[0])):
                if temp < (grid[col][row]):
                    temp = grid[col][row]
            bottom_to_top.append(temp)
        
        temp = 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = min(left_to_right[i],bottom_to_top[j])
                res[i][j] = temp
        
        result = 0        
        # i,j=0,0
        for i in range(len(copy)):
            for j in range(len(copy[0])):
                result = result + abs(copy[i][j] - res[i][j])
        
        return (result)
                
                
        
                
        
        
        
                
        