class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        visited = [ [0]*len(matrix[0]) for _ in range(len(matrix)) ]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                
                width = visited[i][j] = visited[i][j-1]+1 if j else 1
                
                for k in range(i,-1,-1):
                    width = min(width,visited[k][j])
                    maxarea = max(maxarea,width * (i-k+1))
        return maxarea
                