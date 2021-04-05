class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = [0]*2
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.rows[row]+=1
            self.cols[col]+=1
            if row == col:
                self.diagonal[0]+=1
            if row+col ==self.n-1:
                self.diagonal[1]+=1
            if self.rows[row] == self.n or self.cols[col] == self.n or self.diagonal[0] == self.n or self.diagonal[1] == self.n:
                return 1
        else:
            self.rows[row]-=1
            self.cols[col]-=1
            if row == col:
                self.diagonal[0]-=1
            if row+col ==self.n-1:
                self.diagonal[1]-=1
            if self.rows[row] == -self.n or self.cols[col] == -self.n or self.diagonal[0] == -self.n or self.diagonal[1] == -self.n:
                return 2
        return 0
            
                    
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)