class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        visited = [[False for _ in range(cols)]for _ in range(rows)]
        
        def dfs(board,x,y,idx,word):
            if len(word) == 0:
                return True
            if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y]!= word[0]:
                return False
            
            
            board[x][y] = '#'
            
            ret = False
            
            ret = dfs(board,x+1,y,idx+1,word[1:]) or dfs(board,x,y+1,idx+1,word[1:]) or dfs(board,x-1,y,idx+1,word[1:]) or dfs(board,x,y-1,idx+1,word[1:])
            
            # if ret:break
            board[x][y] = word[0]
            return ret
            
        for row in range(rows):
            for col in range(cols):
                if dfs(board,row,col,0,word):
                    return True
        
        return False