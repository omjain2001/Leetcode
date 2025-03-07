# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkHeight(self, root, balanced):
        if root == None: return 0
        left = self.checkHeight(root.left, balanced)
        right = self.checkHeight(root.right, balanced)
        balanced[0] &= (abs(left-right) <= 1)
        return 1 + max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        balanced = [1]
        self.checkHeight(root, balanced)
        return bool(balanced[0])