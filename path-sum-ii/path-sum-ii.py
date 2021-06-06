# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:return []
        # if root.val == targetSum and root.left and root.right:return []
        if root.val == targetSum and not root.left and not root.right:return [[root.val]]
        res = []
        def dfs(root,path):
            if root is None:
                return
            path = path +[root.val]
            if sum(path) == targetSum and len(path)!=1 and root.left is None and root.right is None:
                res.append(path)
            dfs(root.left,path)
            dfs(root.right,path)
        
        dfs(root,[])
        return (res)