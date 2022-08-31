class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        current = head
        
        while current is not None:
            # check for child node
            if current.child is not None:
                # merge child list into our list
                self.child(current)
                
            # move to the next node
            current = current.next
        
        return head
    
    def child(self, current):
        
        child = current.child
        while child.next is not None : #Go the last
            child = child.next
        
        #Child to current.next connect
        if current.next is not None:
            child.next = current.next
            current.next.prev = child
        
        #Connecting current and child
        # child is currently pointing at the last node of the child list, 
        # use pointer (current.child) to get to the first node of the child list
        current.next = current.child
        current.child.prev = current
        
        current.child = None