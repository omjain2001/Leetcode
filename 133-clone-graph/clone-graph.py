"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        hashmap = {}

        def dfs(n):
            
            # Create new node
            newnode = Node(n.val)
            hashmap[n] = newnode

            for adj_node in n.neighbors:
                if adj_node not in hashmap:
                    dfs(adj_node)
                newnode.neighbors.append(hashmap[adj_node])
            
            return newnode

        return dfs(node)
        