# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def height(root):
            if not root:
                return -1
            else:
                return 1+ max(height(root.left),height(root.right))
        
        #calculate height of left subtree
        #calculate height of right subtree
        #check if the differnece if more than one, if yes, return False else return true
        return abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        