# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        # Perform inorder traversal
        stack = []
        curr = root
        count = 0
        while(True):
            while(curr):
                stack.append(curr)
                curr = curr.left
            if len(stack) == 0:
                break
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            curr = node.right
        return -1