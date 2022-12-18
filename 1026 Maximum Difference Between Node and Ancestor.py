# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res =0
        def dfs(node, curr_max,curr_min):
            nonlocal res
            if not node:
                return 
            curr_max, curr_min = max(curr_max, node.val), min(curr_min, node.val)
            res = max(res, curr_max - curr_min)
            dfs(node.left, curr_max, curr_min)
            dfs(node.right, curr_max, curr_min)
        dfs(root, root.val, root.val)
        return res


