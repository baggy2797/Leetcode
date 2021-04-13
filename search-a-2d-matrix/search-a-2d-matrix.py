class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        t_row = 0
        for row in range(rows):
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] < target:
                t_row = row
                continue
            else:
                break
        print(t_row)
        for col in range(cols):
            if matrix[t_row][col] == target:
                return True
        return False
                