# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(inorder) == 0:
            return 
          
        root_val = preorder.pop(0)
        root =  TreeNode(root_val)
        index_root = inorder.index(root_val)
        
        l_lst = inorder[:index_root:]
        r_lst = inorder[index_root+1::]
        
        root.left = self.buildTree(preorder, l_lst)
        root.right = self.buildTree(preorder, r_lst)
        
        
        return root
        
#         if len(inorder) == 0:
#             return 
        
#         val = preorder.pop(0)
#         root = TreeNode(val)
#         idx = inorder.index(val)
        
#         left_tree = inorder[:idx:]
#         right_tree = inorder[idx+1::]
        
#         root.left = self.buildTree(preorder,left_tree)
#         root.right = self.buidTree(preorder,right_tree)
        
#         return root
        
        
        
        