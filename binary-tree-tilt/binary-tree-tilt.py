# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        
        sumTilt = 0
        
        def valueSum(root):
            nonlocal sumTilt
            
            if root is None:
                return 0
            
            leftSum = valueSum(root.left)
            rightSum = valueSum(root.right)
            tilt = abs(leftSum - rightSum)
            sumTilt+= tilt
            return root.val + leftSum + rightSum
    
        valueSum(root)
        return (sumTilt)
                
            
            
            
            
        
            