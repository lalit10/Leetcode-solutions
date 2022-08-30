class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #use a que and use last value at each level        
        if root is None:
            return []
        store = [[root]]
        result = []
        while store:
            level = store.pop()            
            result.append(level[-1].val)        #Last value of that level     
            sub_level = []
            for node in level:
                if node.left:
                    sub_level.append(node.left)
                if node.right:
                    sub_level.append(node.right)
            if sub_level:
                store.append(sub_level)
                
           
        return result