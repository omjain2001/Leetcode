# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = 0
    def recur(self, root: Optional[TreeNode]):
        if root == None: return 0
        left = self.recur(root.left)
        right = self.recur(root.right)
        self.d = max(self.d, left+right)
        return 1 + max(left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recur(root)
        return self.d

        