# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = [root]
        summ = depth = 0
        while level:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            depth+=1  
            level = next_level
            temp = sum(node.val for node in next_level)
            summ = temp if temp!=0 else summ
            
        return summ   