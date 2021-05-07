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
        
        @lru_cache(maxsize=100)
        def valueSum(root):
            if root is None:
                return 0
            res = root.val + valueSum(root.left)+valueSum(root.right)
            return res
        
        level =[root]
        
        while level:
            next_level = []
            
            for node in level:
                
                if node.left:
                    x = valueSum(node.left)
                    next_level.append(node.left)
                else:x = 0
                    
                if node.right:
                    y = valueSum(node.right)
                    next_level.append(node.right)
                else:y = 0
                
                sumTilt += abs(x -y)
            level = next_level
        
        return (sumTilt)
                
            
            
            
            
        
            