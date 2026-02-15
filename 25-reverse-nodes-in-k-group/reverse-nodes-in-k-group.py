# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0:
            return head

        # Determine length of LL
        length = 0
        curr = head
        while(curr):
            length += 1
            curr = curr.next
        
        n = length // k

        def reverseLL(node):
            prev = None
            curr = node
            count = k
            while(curr and count):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
            
            return prev, curr
        

        def recur(node, n):
            if n == 0 or node is None:
                return node
            
            prev, curr = reverseLL(node)

            node.next = recur(curr, n-1)

            return prev
        
        return recur(head, n)
            

        