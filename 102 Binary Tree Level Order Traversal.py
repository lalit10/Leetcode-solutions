class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        store = [[root]]
        result = []
        while store:
            level = store.pop()            
            result.append([node.val for node in level])            
            sub_level = []
            for node in level:
                if node.left:
                    sub_level.append(node.left)
                if node.right:
                    sub_level.append(node.right)
            if sub_level:
                store.append(sub_level)
                
           
        return result