# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         level = [root]
#         l_count,r_count= 0,0
#         res = {}
#         h = 0
#         res[h] = 1
#         while level:
#             next_level = []
            
#             for node in level:
                
#                 if node.left:
#                     l_count +=1
#                     next_level.append(node.left)
                
#                 if node.right:
#                     r_count+=1
#                     next_level.append(node.right)
        
#             level = next_level
        
#         print(l_count,r_count)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def findDepth(root):
            if root is None:
                return 0

            return 1 + max(findDepth(root.left), findDepth(root.right))

        if root is None:
            return 0

        left = findDepth(root.left)
        right = findDepth(root.right)

        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)


        return max(left+right, max(ldia, rdia))
                    



                
                
        