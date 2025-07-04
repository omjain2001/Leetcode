"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        hashmap = {}

        temp = head
        while temp:
            newnode = Node(temp.val)
            hashmap[temp] = newnode
            temp = temp.next

        temp = head
        while temp:
            if temp.next:
                hashmap[temp].next = hashmap[temp.next]
            if temp.random:
                hashmap[temp].random = hashmap[temp.random]
            temp = temp.next

        return hashmap[head]    