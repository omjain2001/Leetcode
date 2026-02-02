# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummyNode = ListNode()
        dummyNode.next = head

        slow = dummyNode
        fast = dummyNode
        while(n and fast):
            fast = fast.next
            n -= 1
        
        if fast is None:
            return head
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next
        slow.next.next = None
        slow.next = temp

        return dummyNode.next
        