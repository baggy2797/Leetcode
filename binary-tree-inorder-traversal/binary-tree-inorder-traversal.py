# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        stack = []
        res = []
        while True:
            while current:
                stack.append(current)
                current = current.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            current = node.right
        print(res)