class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows ,cols = len(matrix),len(matrix[0])
        
        def makerowcolzero(row,col):
            for i in range(rows):
                if matrix[i][col]!=0:
                    matrix[i][col] = "#"
            for j in range(cols):
                if matrix[row][j]!=0:
                    matrix[row][j] = "#"
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    makerowcolzero(row,col)
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "#":
                    matrix[row][col]=0
        print(matrix)
                
                
                
                
        