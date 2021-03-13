# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def generate(start, end):
            res = []
            for root in range(start, end + 1):
                leftTrees = generate(start, root - 1)
                rightTrees = generate(root + 1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res or [None]
        return generate(1, n)