# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = [root]
        total = 0
        while level:
            next_level = []
            for node in level:
                if node.left:
                    if node.left.left is None and node.left.right is None and node.left is not None:
                        total = total + node.left.val
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
        return (total)
                