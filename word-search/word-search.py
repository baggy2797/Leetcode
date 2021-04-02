class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.new = ""
        self.idx = 0
        for row in range(rows):
            for col in range(cols):
                # if board[row][col] == word[0]:
                    
                if self.backtrack(board,row,col,word):
                    # if self.new == word:
                    return True
                    
                    # self.new = ""
                    
        return False
        
    def backtrack(self,board,x,y,word):
        if len(word) == 0:
            return True
        
        if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
            return False
        
        if board[x][y] == word[0]:
            board[x][y] = ""
        
            if self.backtrack(board,x+1,y,word[1:]) or self.backtrack(board,x,y+1,word[1:]) or self.backtrack(board,x-1,y,word[1:]) or self.backtrack(board,x,y-1,word[1:]):
                return True
            board[x][y] = word[0]
        
        return False
        
        
        
        
        
        
#         def backtrack(board,x,y,idx):
#             if x >= rows or y >= cols or x < 0 or y < 0 or idx >= len(word) or board[x][y]!=word[idx] or self.new == word:   
#                 return 
            
#             else:
                
#                 self.new += word[idx]

#                 board[x][y]= ""
#                 print(self.new)
#                 idx+=1
                
#                 backtrack(board,x,y+1,idx)
            
#                 backtrack(board,x+1,y,idx)
                    
#                 backtrack(board,x,y-1,idx)
                    
#                 backtrack(board,x-1,y,idx)
        
        
            
            