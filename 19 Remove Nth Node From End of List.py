class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast= head
        slow = head

        for _ in range(n):  # Take faster node n steps ahead
            fast = fast.next
        
        if not fast: #Return head node as it is n from back
            return head.next
        
        while fast.next: #Iterate over remaining, gives us location of n in slow
            fast= fast.next
            slow = slow.next
        
        slow.next = slow.next.next #Skip the next of slow as needed
        return head

#Time Complexity: O(n)
#Space Complexity: O(1)