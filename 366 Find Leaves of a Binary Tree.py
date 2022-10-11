# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Post Order traversal maar
        #List mei store kar
        if root is None:
            return []
        result = []
        def dfs(root):
            level = 0
            if root.left:
                level = max(level, 1 + dfs(root.left))
            if root.right:
                level = max(level, 1 + dfs(root.right))
            for _ in range(level-len(result)+1):
                result.append([])
            result[level].append(root.val)
            return level
        dfs(root)
        return result

# Another Solution
# class Solution:
#     def __init__(self):
#         self.height = defaultdict(list)
#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         def dfs(node):
#             if not node:
#                 return -1
            
#             leftHeight = dfs(node.left)
#             rightHeight = dfs(node.right)
#             h = max(leftHeight, rightHeight)+1
#             self.height[h].append(node.val)
#             return h
#         dfs(root)
#         #a = sorted(self.height)
#         #res = [self.height[k] for k in a]
#         return self.height.values()