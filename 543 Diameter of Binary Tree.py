# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Post order traversal
        result = 0
        def postOrderTraversal(node):
            nonlocal result
            if node:
                left = postOrderTraversal(node.left)
                right = postOrderTraversal(node.right)
                result = max(result, left+right)
                height = max(left, right) + 1
                return height
            return 0
        postOrderTraversal(root)
        return result