# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #Recursion mei check kar
        #Conditions
        #1. Equal 
        #2. Diff

        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.right) and\
        self.flipEquiv(root1.right, root2.left) ) or \
        (self.flipEquiv(root1.left, root2.left) and\
        self.flipEquiv(root1.right, root2.right))

#Time complexity: O(min(m,n)) where m and n are the number of nodes in the two trees
#Space complexity: O(min(h1,h2)) where h1 and h2 are the height of the two trees