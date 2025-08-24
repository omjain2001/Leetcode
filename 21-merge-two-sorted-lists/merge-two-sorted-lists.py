# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head = list1 if (list1.val <= list2.val) else list2

        c1 = list1
        c2 = list2
        curr = None

        while(c1 and c2):
            if c1.val <= c2.val:
                if curr:
                    curr.next = c1
                curr = c1
                c1 = c1.next
            else:
                if curr:
                    curr.next = c2
                curr = c2
                c2 = c2.next
        
        if c1:
            curr.next = c1
        else:
            curr.next = c2
        
        return head
        