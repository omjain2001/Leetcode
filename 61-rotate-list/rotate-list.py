# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        length = 0
        curr = head
        while(curr):
            length += 1
            curr = curr.next
        
        rotations = k % length

        if rotations == 0:
            return head

        dummyNode = ListNode()
        dummyNode.next = head

        slow = dummyNode
        fast = dummyNode
        for i in range(rotations):
            fast = fast.next
        
        while(fast.next):
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        slow.next = None
        fast.next = head

        return temp
        