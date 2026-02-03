# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if root is None or target is None:
            return None
        
        parent_map = {}
        parent_map[root] = None

        def recur(node):
            if node is None:
                return node

            if node.left:
                parent_map[node.left] = node
                recur(node.left)
            
            if node.right:
                parent_map[node.right] = node
                recur(node.right)
            
        recur(root)

        queue = deque()
        queue.append(target)

        visited = set()
        visited.add(target)

        while(len(queue) > 0 and k):
            queue_length = len(queue)
            while(queue_length):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if parent_map[node] and parent_map[node] not in visited:
                    queue.append(parent_map[node])
                    visited.add(parent_map[node])
                queue_length -= 1
            k -= 1
        
        result = [node.val for node in queue]
        return result
        
            

