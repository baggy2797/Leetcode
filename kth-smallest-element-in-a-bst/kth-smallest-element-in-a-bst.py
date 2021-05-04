# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = []
        self.k = k
        self.inorder(root)
        return self.res[-1]
        
    def inorder(self,node):
        if node is None:return
        self.inorder(node.left)
        if len(self.res) == self.k:
            return
        self.res.append(node.val)
        self.inorder(node.right)
    
        
            
            
        