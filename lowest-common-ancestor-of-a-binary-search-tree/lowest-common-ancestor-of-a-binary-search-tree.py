# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root.val
        pValue,qValue = p.val,q.val
        
        if pValue > node and qValue > node:
            return self.lowestCommonAncestor(root.right,p,q)
        elif pValue < node and qValue < node:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root