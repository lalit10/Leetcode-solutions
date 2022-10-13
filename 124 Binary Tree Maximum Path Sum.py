# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')        
        
        def pathSum(node):
            nonlocal result
            if not node:
                return 0
            left = pathSum(node.left)
            right = pathSum(node.right)
            result = max(result, node.val + left + right)
            return max(node.val +(max(left,right)), 0)
        
        pathSum(root)
        return result