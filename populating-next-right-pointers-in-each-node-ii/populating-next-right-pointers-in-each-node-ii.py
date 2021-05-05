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
        if root is None:
            return root
        level = [root]
        root.next = None
        while level:
            next_level = []
            
            for node in level:

                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            
            # for i in range(len(next_level)):
            #     print(next_level[i].val)
            if next_level:
                prev = next_level[0]
            
                for i in range(1,len(next_level)):
                    prev.next = next_level[i]
                    prev = next_level[i]
                    
            # print("\n")
            level = next_level
        
        return root 