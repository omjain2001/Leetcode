# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        curr = head.next
        while(curr):
            if curr.val == prev.val:
                next = curr.next
                curr.next = None
                prev.next = next
                curr = next
            else:
                prev = curr
                curr = curr.next
        
        return head

        