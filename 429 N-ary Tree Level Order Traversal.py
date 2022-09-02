class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return None
        queue = collections.deque([root])  #Create a queue to store the nodes
        result = []
        while queue:
            level =[]
            for _ in range(len(queue)):
                current = queue.popleft()                
                level.append(current.val)   #Add the value of the current node to the level
                for child in current.children:  #Add the children of the current node to the queue
                    if child:
                        queue.append(child)
            result.append(level)
        return result