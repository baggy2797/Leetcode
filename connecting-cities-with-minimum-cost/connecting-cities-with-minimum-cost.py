class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        neighbor = defaultdict(list)
        for i,j,c in connections:
            neighbor[i].append((j,c))
            neighbor[j].append((i,c))
        
        res = 0
        mini_heap = [(0,1)]
        visited = set()
        
        while mini_heap:
            c,i = heappop(mini_heap)
            if i in visited:
                continue
            else:
                visited.add(i)
                res += c
                
                if len(visited) == N:
                    return res
                else:
                    for j,c in neighbor[i]:
                        if j is visited:
                            continue
                        else:
                            heappush(mini_heap,(c,j))
                            
        return -1