# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        a = TreeNode(0)
        st = [root]
        while st:
            p = st.pop()
            if p.right:
                st.append(p.right)
            if p.left:
                st.append(p.left)
            a.right = p
            p.left = None
            a = a.right
        if not root:
            return None
        