# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        result = []
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            count = len(queue)
            temp = []
            while count > 0:
                node = queue[0]
                queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                count -= 1
            result.append(temp)
        return result

                