class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def binTree(node, left, right):
            if not node: 
                return True
            if not left < node.val < right:
                return False
            return binTree(node.left, left, node.val ) and binTree(node.right, node.val, right )
        return binTree(root,float('-inf'), float('inf'))