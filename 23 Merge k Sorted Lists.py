# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Brute force is creating a new linkedin list and storing original values in a list and sorting them and appending to new list
        #Put all the items on a priority queue and pop one each
        curr = ListNode()
        dummy = curr
        store = []
        for i in range(len(lists)):
            while lists[i] is not None:
                store.append(lists[i].val)
                lists[i] = lists[i].next
        #print("Store is:-", store)
        store.sort()
        for i in store:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        
#Use of heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr
        store = []

        for i in range(len(lists)):
            while lists[i] is not None:
                heapq.heappush(store, lists[i].val)
                lists[i] = lists[i].next
        while store:
            curr.next = ListNode(heapq.heappop(store))
            curr = curr.next
        return dummy.next

#Heapq with tuple
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        store = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(store, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while store:
            val, i = heapq.heappop(store)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(store, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next
