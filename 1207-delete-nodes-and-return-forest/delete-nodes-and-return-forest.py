from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        result = []
        to_delete = set(to_delete)

        queue = deque()

        queue.append(root)

        def recur(node):
            if node is None:
                return None
            if node.val in to_delete:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                return None
            
            node.left = recur(node.left)
            node.right = recur(node.right)

            return node
        

        while(len(queue) > 0):
            node = queue.popleft()
            res = recur(node)
            if res is not None:
                result.append(res)

        return result
         
        