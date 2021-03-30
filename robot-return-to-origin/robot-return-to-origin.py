class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y =0
        for move in moves:
            if move == "U":
                y = y+1
            elif move =="D":
                y = y-1
            elif move == "L":
                x = x-1
            elif move == "R":
                x = x+1
        
        return x==0 and y==0