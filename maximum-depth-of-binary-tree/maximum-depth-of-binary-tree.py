# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        
        level =[root]
        height = 0
        while level:
            next_level = []
            for node in level:

                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            height+=1
            level = next_level
        
        return (height)