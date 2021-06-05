# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        
        def getLonely(root):
            if root is None:return
            if (root.left and not root.right):res.append(root.left.val)
            if (root.right and not root.left):res.append(root.right.val)
            getLonely(root.left)
            getLonely(root.right)
                
        getLonely(root)
        return (res)
                