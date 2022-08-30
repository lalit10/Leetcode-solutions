class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #In inorder, we go from left to right. Use this to find the kth smallest element by popping from the stack.
        #Use que and store left entirely first, subtract 1 from k and check k
        #if k ==0 return that val, else go to right
        store = []
        while root or store:
            while root:
                store.append(root)
                root = root.left
            root = store.pop()                    
            k -=1
            if k == 0:
                return root.val
            root = root.right