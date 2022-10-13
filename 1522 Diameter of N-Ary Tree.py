"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
        
            max_depth = 0
            for child in node.children:
                depth = 1 + dfs(child)
                diameter = max(diameter, depth + max_depth)
                max_depth = max(max_depth, depth)
    
            return max_depth
        
        diameter = 0
        dfs(root)        
        return diameter
        

#Time Complexity: O(n)
#Space Complexity: O(n)