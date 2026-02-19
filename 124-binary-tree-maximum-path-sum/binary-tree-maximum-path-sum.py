# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxi = -1e10

        def recur(node):
            nonlocal maxi
            if node is None:
                return 0
            
            left = recur(node.left)
            right = recur(node.right)

            maxi = max(maxi, node.val + left + right)

            return max(node.val + max(left, right), 0)
        
        recur(root)

        return maxi



        