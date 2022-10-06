class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root:
            return 0, float("inf"), float("-inf")
        left_count, left_min, left_max = self.dfs(root.left)
        right_count, right_min, right_max = self.dfs(root.right)
        if left_max < root.val < right_min:
            return left_count + right_count + 1, min(left_min, root.val), max(right_max, root.val)
        return max(left_count, right_count), float("-inf"), float("inf")