# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        def dfs(root,path):
            if root is None:
                return
                
            if root.left is None and root.right is None:
                paths.append(path+str(root.val))
            
            path = path + str(root.val)+'->'
            dfs(root.left,path)
            dfs(root.right,path)
        
        dfs(root,"")
        return (paths)
            
            