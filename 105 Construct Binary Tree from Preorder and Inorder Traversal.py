class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Preorder first element is the root
        #Split inorder on the basis of root and create the tree
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            #print("Preorder is:-", preorder)
            root = TreeNode(inorder[root_index])
            #print("Left side is:", inorder[0:root_index])
            #print("Right side is:", inorder[root_index+1:])
            root.left = self.buildTree(preorder, inorder[0:root_index])
            root.right = self.buildTree(preorder, inorder[root_index+1:])
            return root