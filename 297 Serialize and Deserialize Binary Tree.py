# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Preorder traversal recursive should work
#Iterative a deque can be used 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorder(node):
            if not node:
                result.append("#")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        #print("Result in serialize is:-", result)
        return ",".join(result)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        count = 0
        def preorder():
            nonlocal count
            if data[count] == "#":
                count+=1
                return
            root = TreeNode(int(data[count]))
            count+=1
            root.left = preorder()
            root.right = preorder()
            #print("Root in deserialize is:-", root)
            return root
        
        return preorder()
        
#Time Complexity: O(n)
#Space Complexity: O(n)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))