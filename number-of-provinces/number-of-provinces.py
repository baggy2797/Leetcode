class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = [0 for _ in range(length)]
        
        count = 0
        
        def dfs(isConnected,visited,i):
            for j in range(length):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(isConnected,visited,j)
                
    
        for i in range(length):
            if visited[i] == 0:
                dfs(isConnected,visited,i)
                count+=1
            
        return count