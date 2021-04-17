class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        outDegree = {}
        for edge in edges:
            outDegree[edge[0]] = outDegree.get(edge[0],0)+1
            outDegree[edge[1]] = outDegree.get(edge[1],0)+1
        length = len(edges)
        for node,value in outDegree.items():
            if value > length-1:

                return node