# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preorder(p)   == self.preorder(q)
        
    def preorder(self,root):
        if root is None:
            return ""
        
        return str(root.val)+" " + self.preorder(root.left)+" "+self.preorder(root.right)
    
    