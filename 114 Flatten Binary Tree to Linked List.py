class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #Use a stack and append to stack
        if not root: 
            return None
        
        stack = [root]
        while len(stack):
            root = stack.pop()
            
            if root.right: 
                stack.append(root.right)
            if root.left: 
                stack.append(root.left)
                
            root.left = None
            if len(stack):
                root.right = stack[-1] 
            else:
                None
                
# O(1) space and O(n) time
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
    
        root.right = self.prev
        root.left = None
        self.prev = root