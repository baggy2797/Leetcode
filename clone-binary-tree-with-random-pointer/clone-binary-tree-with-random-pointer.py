# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        
        level = [root]
        copy = {}
        while level:
            next_level = []
            
            for node in level:
                copy[node] = NodeCopy(node.val)
                # print(node.val)
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
                # if node.random:
                #     next_level.append(node.random)
            
            level = next_level
            
        
        level = [root]
        
        while level:
            next_level = []
            
            for node in level:
                
                if node.left:
                    copy[node].left = copy[node.left]
                    next_level.append(node.left)
                
                if node.right:
                    copy[node].right = copy[node.right]
                    next_level.append(node.right)
                    
                if node.random:
                    copy[node].random = copy[node.random]

            
            level = next_level
        
        return copy[root]
        
                
                