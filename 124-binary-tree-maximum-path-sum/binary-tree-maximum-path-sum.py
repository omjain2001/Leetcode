# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = -3 * 10**7
    def recur(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.recur(root.left)
        right = self.recur(root.right)
        
        # Update maximum
        self.maxi = max(self.maxi, left + right + root.val)
        val = max(root.val, root.val + max(left, right))
        if val < 0:
            return 0
        return val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.recur(root)
        return self.maxi
        