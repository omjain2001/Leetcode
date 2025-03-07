# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, mini, maxi):
        if root == None: return True
        if root.val <= mini or root.val >= maxi: return False
        return self.recur(root.left, mini, root.val) and self.recur(root.right, root.val, maxi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root, -2**31-1, 2**31)


