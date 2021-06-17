class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        
        for i,route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        
        ans = 0
        
        queue = collections.deque([source])
        seen = set()
        rseen = set()
        
        seen.add(source)
        
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                
                for routeId in graph[stop]:
                    if routeId not in rseen:
                        rseen.add(routeId)
                        for new_stop in routes[routeId]:
                            if new_stop not in seen:
                                queue.append(new_stop)
                                seen.add(new_stop)
            ans+=1
        
        return -1