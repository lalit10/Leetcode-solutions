class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #Function for making a copy
        #If not in store, add to store, append to stack
        #update neighbours
        if not node: 
            return
        store = {node: Node(node.val)}
        stack = [node]
        while stack:
            currentNode = stack.pop()
            for neighbour in currentNode.neighbors:
                if neighbour not in store:
                    store[neighbour] = Node(neighbour.val)
                    stack.append(neighbour)
                store[neighbour].neighbors.append(store[currentNode])
        return store[node] # return the value of the original node which is a copy of that original node