class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result+=matrix.pop(0)
            print(result)
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
        
        return result