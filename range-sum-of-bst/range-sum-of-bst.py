# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        summ = 0
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node:
                    if low <= node.val and node.val <= high:
                        summ += node.val
                    if low < node.val:
                        next_level.append(node.left)
                    if node.val < high:
                        next_level.append(node.right)
            level = next_level
        return summ
                    
                    
