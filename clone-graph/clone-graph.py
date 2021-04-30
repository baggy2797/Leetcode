"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node is None:
            return node
        
        visited = {}
        q = collections.deque([node])
        visited[node] = Node(node.val, [])

        while q:            
            elem = q.pop()
            for neighbor in elem.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                visited[elem].neighbors.append(visited[neighbor])

        return visited[node]