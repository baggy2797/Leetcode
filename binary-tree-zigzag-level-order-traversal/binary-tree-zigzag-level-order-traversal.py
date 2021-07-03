# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        level = [root]
        result = [[root.val]]
        
        reverse = True
        while level:
            next_level = []
            temp = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    temp.append(node.right.val)
            # print(temp.reverse(),reverse)
            if reverse:
                if temp:
                    # temp.reverse()
                    result.append(temp[::-1])
            else:
                if temp:
                    result.append(temp)
            reverse = not reverse
            level = next_level
        return(result)