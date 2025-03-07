# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        queue = []
        result = []
        queue.append(root)
        while(len(queue) > 0):
            count = len(queue)
            node = queue[-1]
            result.append(node.val)
            while(count > 0):
                node = queue[0]
                queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                count -= 1

        return result

