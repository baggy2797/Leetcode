class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # pass
        M, N = len(matrix), len(matrix[0])
        MOVES = [(1,0), (0,1), (-1,0), (0,-1)]
        
        @functools.cache
        def dfs(i, j):
            path_length = 0
            for di, dj in MOVES:
                ni, nj = i+di, j+dj
                if 0<=ni<M and 0<=nj<N and matrix[ni][nj] > matrix[i][j]:
                    path_length = max(path_length, dfs(ni, nj))
            return 1 + path_length
        
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))
        
        return res
#         rows = len(matrix)
#         cols = len(matrix[0])
#         MOVES = [(1,0),(0,1),(-1,0),(0,-1)]
        
#         def dfs(x,y):
#             pathLength = 0
#             for di,dj in MOVES:
#                 ni,nj = x+di,y+dj
                
#                 if 0<=ni<rows and 0<=nj<cols and matrix[ni][nj] > matrix[x][y]:
#                     pathLength = max(pathLength,dfs(ni,nj))
#             return 1+pathLength
            
#         res = 0
#         for row in range(rows):
#             for col in range(cols):
#                 res = max(res,dfs(row,col))
#         return res