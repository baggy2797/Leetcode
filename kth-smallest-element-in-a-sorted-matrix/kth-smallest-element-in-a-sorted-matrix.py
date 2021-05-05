class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for value in row:
                if len(heap) < k:
                    heapq.heappush(heap,-1*value)
                else:
                    heapq.heappushpop(heap, -1*value)
    
        root = -1*heap[0]
        return root