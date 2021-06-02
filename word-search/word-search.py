class Solution:
    def dfs(self,board,x,y,word):
        if len(word) == 0:return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y]!= word[0]:
            return False
        temp = board[x][y] 
        board[x][y] = '#'
        ret = self.dfs(board,x+1,y,word[1:]) or self.dfs(board,x,y+1,word[1:]) or self.dfs(board,x-1,y,word[1:]) or self.dfs(board,x,y-1,word[1:])
        board[x][y] = temp    
        return ret
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.dfs(board,row,col,word):return True
        return False
                
            