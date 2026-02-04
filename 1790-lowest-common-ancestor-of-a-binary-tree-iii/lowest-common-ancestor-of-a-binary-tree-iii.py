"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        if q is None or p is None:
            return None
        
        hashset = set()

        while(p and q):
            if p in hashset:
                return p
            hashset.add(p)
            if q in hashset:
                return q
            hashset.add(q)

            p = p.parent
            q = q.parent
        
        while p:
            if p in hashset:
                return p
            p = p.parent

        while q:
            if q in hashset:
                return q
            q = q.parent
        return None
        
        