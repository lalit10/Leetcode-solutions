# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(node, res):
            if node:
                res -= node.val
            else:
                return None
            if (res == 0) and (node.left == node.right==None):
                return True
            else:
                return path(node.left, res) or path(node.right, res)
        return path(root,targetSum)

#Time Complexity: O(n)
#Space Complexity: O(logn)