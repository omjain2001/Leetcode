# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head is None:
            return None

        def recur(node):
            slow = node
            fast = node
            prev = None
            while(fast.next is not None and fast.next.next is not None):
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev is not None:
                prev.next = None

            newnode = TreeNode(slow.val)
            
            if slow != node:
                newnode.left = recur(node)
            if slow.next is not None:
                temp = slow.next
                slow.next = None
                newnode.right = recur(temp)
            
            return newnode
        
        return recur(head)
            
