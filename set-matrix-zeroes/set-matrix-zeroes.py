class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        #set rows
        for element in rows:
            for col in range(len(matrix[0])):
                matrix[element][col] = 0
        
        # set cols
        for row in range(len(matrix)):
            for element in cols:
                matrix[row][element] = 0
            
        
                    