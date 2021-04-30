# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # currSum = 0
        
        def dfs(node,currSum):
            if node is None:return False
            currSum += node.val
            if node.left is None and node.right is None and targetSum == currSum:return True
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        return dfs(root,0)