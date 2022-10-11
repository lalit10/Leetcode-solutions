# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        queue = []

        node = root
        queue.append([node,0])
        store = {}
        
        while len(queue) > 0:
            node,level = queue.pop(0)
            
            if level not in store:
                store[level] = [node.val]
            else:
                store[level].append(node.val)
            
            if node.left is not None:
                queue.append([node.left,level-1])
            if node.right is not None:
                queue.append([node.right,level+1])
        
        sortedkeys = sorted(store.keys())
        result = []
        for i in sortedkeys:
            result.append(store[i])
        return result


#Level Order Traversal - BFS