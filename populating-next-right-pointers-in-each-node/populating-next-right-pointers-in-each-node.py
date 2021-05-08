"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = [root]
        while level:
            next_level = []
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            for i in range(1,len(next_level)):
                next_level[i-1].next = next_level[i]
                
            level = next_level
        return root