# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None 
        head = None  

        while(l1 and l2):
            total = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            newnode = ListNode(total)
            if prev is None:
                prev = newnode
                head = newnode
            else:
                prev.next = newnode
                prev = newnode
            l1 = l1.next
            l2 = l2.next
        
        while(l1):
            total = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            newnode = ListNode(total)
            if prev is None:
                prev = newnode
                head = newnode
            else:
                prev.next = newnode
                prev = newnode
            l1 = l1.next
        
        while(l2):
            total = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            newnode = ListNode(total)
            if prev is None:
                prev = newnode
                head = newnode
            else:
                prev.next = newnode
                prev = newnode
            l2 = l2.next

        if carry > 0:
            newnode = ListNode(carry)
            prev.next = newnode
            prev = newnode

        return head