class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        rows,cols = len(rooms),len(rooms[0])
        queue = collections.deque([])
        
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row,col))
        
        while queue:
            l = queue.popleft()
            row,col = l[0],l[1]
            for direction in directions:
                r,c = row + direction[0],col+direction[1]
                if r >=0 and r<rows and c>=0 and c<cols and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col]+1
                    queue.append((r,c))