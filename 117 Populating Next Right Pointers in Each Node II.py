class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            for index in range(len(queue)-1):
                queue[index].next = queue[index+1]
        return root