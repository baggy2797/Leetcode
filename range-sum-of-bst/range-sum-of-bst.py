# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        level = [root]
        self.sum = 0
        while level:
            next_level = []
            
            for node in level:
                if node.val >=low and node.val<=high:
                    self.sum += node.val
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)
                        
            level = next_level
            
        return (self.sum)
                    