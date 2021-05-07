class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]* len(isConnected)
        rows,cols = len(isConnected),len(isConnected[0])
        
        def dfs(isConnected,visited,i):
            for j in range(cols):
                if isConnected[i][j]==1 and visited[j]==0:
                    visited[j] =1
                    dfs(isConnected,visited,j)
        
        count = 0
        for i in range(rows):
            if visited[i] == 0:
                dfs(isConnected,visited,i)
                count+=1
        return count
        