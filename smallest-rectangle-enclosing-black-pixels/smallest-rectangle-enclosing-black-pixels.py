class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        
        rows,cols = len(image),len(image[0])
        if rows == 0 or cols == 0:
            return 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        self.top,self.bottom = x,x
        self.left,self.right =y,y
        def dfs(image,x,y,visited):
            if x < 0 or y < 0 or x >= rows or y >= cols or visited[x][y] == 1 or image[x][y]!="1":
                return
            
            self.top = min(self.top,x)
            self.bottom = max(self.bottom,x+1)
            self.left = min(self.left,y)
            self.right = max(self.right,y+1)
            
            
            visited[x][y] = 1
            dfs(image,x+1,y,visited)
            dfs(image,x,y+1,visited)
            dfs(image,x-1,y,visited)
            dfs(image,x,y-1,visited)
        
        dfs(image,x,y,visited)
        return abs(self.bottom-self.top) * abs(self.right - self.left)