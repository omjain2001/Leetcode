# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-1000,None)
        prev = head
        curr = head.next
        dups = set()
        while curr:
            if curr.val == prev.val:
                dups.add(curr.val)
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        prev = dummy
        curr = head
        while curr:
            if curr.val in dups:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        prev.next = None
        return dummy.next
        
        