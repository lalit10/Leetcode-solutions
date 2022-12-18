# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        #Get total sum 
        #Iterate over tree and do multiplication
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total_sum = totalSum(root)
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_sum = node.val + left_sum + right_sum
            res = max(res, (total_sum - curr_sum) * curr_sum)
            return curr_sum
        
        dfs(root)
        return res % (10**9 + 7)


            