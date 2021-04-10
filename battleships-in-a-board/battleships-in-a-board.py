class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows,cols = len(board),len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        if not board:
            return 0
        count = 0
        
        def dfs(x,y):
            if x<0 or x>=rows or y<0 or y>=cols or visited[x][y]==1:
                return
            visited[x][y] = 1
            if board[x][y] =='X':
                dfs(x+1,y)
                dfs(x,y+1)
                dfs(x-1,y)
                dfs(x,y-1)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X' and visited[row][col]==0:
                    dfs(row,col)
                    count+=1
        
        return count
                
        
                