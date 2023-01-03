# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        curr = result

        while list1 and list2:
            v1  = list1.val if list1 else 0
            v2  = list2.val if list2 else 0

            if v1 <= v2:
                curr.next = ListNode(v1)
                list1 = list1.next
            else:
                curr.next = ListNode(v2)
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return result.next


