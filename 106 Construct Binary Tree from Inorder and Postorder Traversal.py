class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Postorder last element is root
        #Split in-order on the basis of root
        if inorder:
            root_index = inorder.index(postorder.pop())
            #print("postorder is:-", postorder)
            root = TreeNode(inorder[root_index])
            #print("Left side is:", inorder[0:root_index])
            #print("Right side is:", inorder[root_index+1:])
            root.right = self.buildTree(inorder[root_index+1:], postorder) #Changed this
            root.left = self.buildTree(inorder[:root_index], postorder)
                        
            return root