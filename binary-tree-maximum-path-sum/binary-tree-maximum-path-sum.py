# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = (-1)*sys.maxsize
        def rec(root):
            if root:
                # print(root.val)
                left,right = max(0,rec(root.left)),max(0,rec(root.right))
                self.res = max(self.res,left + root.val+right)
                return max((root.val+left),(root.val+right))
            else:
                return 0
        rec(root)
        return self.res