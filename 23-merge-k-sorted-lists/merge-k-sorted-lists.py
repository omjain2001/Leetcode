# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Create dummy node
        dummyNode = ListNode(-1)
        
        # Create min heap
        pq = []
        heapq.heapify(pq)

        count = 0

        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, count, node))
                count += 1
        
        curr = dummyNode
        while(len(pq) > 0):
            val, _, node = heapq.heappop(pq)
            curr.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, count, node.next))
                count += 1
            curr = curr.next
        
        return dummyNode.next

        