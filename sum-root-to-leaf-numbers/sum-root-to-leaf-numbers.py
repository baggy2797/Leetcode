# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        summ = 0
        stack = [(root,0)]
        
        while stack:
            root,curr = stack.pop()
            
            if root is not None:
                curr = curr * 10 + root.val
                
                if root.left is None and root.right is None:
                    summ += curr
                else:
                    stack.append((root.right,curr))
                    stack.append((root.left,curr))
        return summ