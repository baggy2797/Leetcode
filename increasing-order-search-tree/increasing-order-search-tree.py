# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp = []
        level = [root]
        
        while level:
            next_level =[]
            for node in level:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
            
        temp = sorted(temp)
        res = dummy = TreeNode(0)
        dummy.left = None
        
        for i in range(len(temp)):
            if i==0:
                new = TreeNode(temp[i])
                new.left = None
                dummy.right = new
                dummy = dummy.right
            else:
                new = TreeNode(temp[i])
                dummy.right = new
                new.left = None
                dummy = dummy.right
        
        return (res.right)
                
                
                
                
            