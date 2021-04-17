# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        level = [(root,None,None)]
        summ = 0
        while level:
            next_level = []
            for node,parent,grandParent in level:
                if grandParent and grandParent.val%2 == 0:
                    summ += node.val
                if node.left:
                    next_level.append((node.left,node,parent))
                if node.right:
                    next_level.append((node.right,node,parent))

            level = next_level
        return summ