"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        clone = {}
        
        q = collections.deque([root])
        
        while q:
            node = q.pop()
            # print(node.val)
            clone[node] = Node(node.val)
            for child in node.children:
                q.append(child)
                
        q.append(root)
        while q:
            node = q.pop()
            # print(node.val)
            # clone[node] = Node(node.val)
            for child in node.children:
                clone[node].children.append(clone[child])
                q.append(child)
        
        return clone[root]
            