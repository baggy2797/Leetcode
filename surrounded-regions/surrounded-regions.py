class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return
        
        rows,cols = len(board),len(board[0])
        

        def dfs(x,y):
        #if the cell is not on the boundary: we can flip it to make it a 'X' and it must previously be a 'O'
            if x < 0 or x >= rows or  y < 0 or y>=cols or board[x][y]!="O":
                return
            # if x ==0 or x == rows-1 or y==0 or y == cols-1:
            #     return
            board[x][y] = "*"
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            
            
        for row in range(rows):
            if board[row][0] == "O": dfs(row,0)
            if board[row][cols-1] == "O": dfs(row,cols-1)
                
            
        for col in range(cols):
            if board[0][col] == "O": dfs(0,col)
            if board[rows-1][col] == "O": dfs(rows-1,col)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":board[row][col] = "X"
                elif board[row][col] == "*":board[row][col] ="O"
                    
                    