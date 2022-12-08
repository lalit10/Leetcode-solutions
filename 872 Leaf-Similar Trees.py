# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Iterative mei last level le sakta
        #DFS mei bhi last level list mei daal and just compare
        def dfs(root):
            result = []

            if root is None:
                return result
            if root.left is None and root.right is None:
                result.append(root.val)

            result += dfs(root.left)
            result += dfs(root.right)

            return result

            
        return dfs(root1) == dfs(root2)

# Time Complexity: O(N)
# Space Complexity: O(N)

#Another Solution
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Iterative mei last level le sakta
        #DFS mei bhi last level list mei daal and just compare
        def iter(root):
            stack = [root]
            result = []
            while stack:
                curr = stack.pop()
                if curr is None:
                    continue
                if curr.left is None and curr.right is None:
                    result.append(curr.val)
                else:
                    stack.append(curr.left)
                    stack.append(curr.right)

            return result            
        return iter(root1) == iter(root2)