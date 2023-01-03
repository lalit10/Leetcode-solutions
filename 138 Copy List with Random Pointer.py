"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        if not head:
            return 
        curr = head

        while curr:
            store[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                store[curr].random = store[curr.random]
            if curr.next:
                store[curr].next = store[curr.next]
            curr = curr.next

        return store[head] 

#Time Complexity: O(n)
#Space Complexity: O(n)