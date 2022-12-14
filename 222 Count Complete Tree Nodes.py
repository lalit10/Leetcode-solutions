# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.right) + self.countNodes(root.left) 
        

#Time complexity: O(n)
#Space complexity: O(logn)


#Another Solution
# class Solution:
#     def compute_depth(self, node: TreeNode) -> int:
#         """
#         Return tree depth in O(d) time.
#         """
#         d = 0
#         while node.left:
#             node = node.left
#             d += 1
#         return d

#     def exists(self, idx: int, d: int, node: TreeNode) -> bool:
#         """
#         Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
#         Return True if last level node idx exists. 
#         Binary search with O(d) complexity.
#         """
#         left, right = 0, 2**d - 1
#         for _ in range(d):
#             pivot = left + (right - left) // 2
#             if idx <= pivot:
#                 node = node.left
#                 right = pivot
#             else:
#                 node = node.right
#                 left = pivot + 1
#         return node is not None
        
#     def countNodes(self, root: TreeNode) -> int:
#         # if the tree is empty
#         if not root:
#             return 0
        
#         d = self.compute_depth(root)
#         # if the tree contains 1 node
#         if d == 0:
#             return 1
        
#         # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
#         # Perform binary search to check how many nodes exist.
#         left, right = 1, 2**d - 1
#         while left <= right:
#             pivot = left + (right - left) // 2
#             if self.exists(pivot, d, root):
#                 left = pivot + 1
#             else:
#                 right = pivot - 1
        
#         # The tree contains 2**d - 1 nodes on the first (d - 1) levels
#         # and left nodes on the last level.
#         return (2**d - 1) + left

# Time complexity: O(d^2) = O(logn^2)
# Space complexity: O(1)