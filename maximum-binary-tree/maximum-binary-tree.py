# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return nums
        
        root = TreeNode()
        root.val = max(nums)
        idx = nums.index(root.val)
        if len(nums[:idx]):
            root.left = self.constructMaximumBinaryTree(nums[:idx])
        if len(nums[idx+1:]):
            root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        
        return root