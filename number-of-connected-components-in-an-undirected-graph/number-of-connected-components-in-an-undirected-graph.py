class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        count = 0
        seen = set()
        
        for i in range(n):
            if i not in seen:
                q = collections.deque([])
                q.append(i)
                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
		
                count += 1
		# Return the count.
        return count
            
        
                    
        