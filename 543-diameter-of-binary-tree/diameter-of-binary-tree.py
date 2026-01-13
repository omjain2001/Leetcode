# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # For each node, the path will be left + root + right.
        # return 1 + max(left, right)

        maxi = 0

        def recur(node):
            nonlocal maxi
            if node is None:
                return 0
            
            left = recur(node.left)
            right = recur(node.right)
            
            maxi = max(maxi, 1 + left + right)

            return 1 + max(left, right)
        
        recur(root)

        return maxi-1
        