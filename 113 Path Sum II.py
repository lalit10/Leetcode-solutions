# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def path(root, targetSum, currentPath):
            nonlocal result
            if root:
                currentPath.append(root.val)
                if not root.left and not root.right and targetSum - root.val ==0:
                    result.append(currentPath)
                path(root.left, targetSum- root.val, currentPath[:])
                path(root.right,targetSum- root.val, currentPath[:])
        path(root, targetSum, [])
        return result
                    
#Time Complexity: O(n)