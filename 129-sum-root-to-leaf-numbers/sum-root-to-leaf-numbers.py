# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total = 0

        if root is None:
            return 0

        def recur(node, val):
            nonlocal total
            if node is None:
                return 0
            
            curr_val = val*10 + node.val

            if node.left is None and node.right is None:
                total += curr_val
                return 0

            recur(node.left, curr_val)
            recur(node.right, curr_val)

        
        recur(root,0)
        
        return total



        