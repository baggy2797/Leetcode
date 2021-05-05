class Solution:
    def dfsToFirstIsland(self,A,x,y):
            if x >= len(A) or x < 0 or y < 0 or y >= len(A[0]) or A[x][y] == 0 or A[x][y] == 2:
                return
            A[x][y] = 2
            self.dfsToFirstIsland(A,x+1,y)
            self.dfsToFirstIsland(A,x,y+1)
            self.dfsToFirstIsland(A,x-1,y)
            self.dfsToFirstIsland(A,x,y-1)
    
    def dfsToReachSecondIsland(self,A,x,y,color):
            if x >= len(A) or x <0 or y >=len(A[0]) or y < 0 :
                return False
            if A[x][y] ==0:
                A[x][y] = color+1
            
            return A[x][y] == 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        if A is None:
            return 0
        flag = False
        rows,cols = len(A),len(A[0])
        
        for i in range(rows):
            if flag:
                break
            for j in range(cols):
                if A[i][j]==1:
                    self.dfsToFirstIsland(A,i,j)
                    flag =True
                    break
        
        for color in range(2,2+rows+cols+1):
            for i in range(rows):
                for j in range(cols):
                    if A[i][j] == color and ( self.dfsToReachSecondIsland(A,i+1,j,color) or self.dfsToReachSecondIsland(A,i,j+1,color) or self.dfsToReachSecondIsland(A,i-1,j,color) or self.dfsToReachSecondIsland(A,i,j-1,color) ):
                        return color-2     