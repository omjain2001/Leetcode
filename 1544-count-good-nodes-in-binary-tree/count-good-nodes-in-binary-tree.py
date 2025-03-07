# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root, maxi):
        if root == None: return 0
        ans = 1 if (root.val >= maxi) else 0
        return ans + self.recur(root.left, max(root.val, maxi)) + self.recur(root.right, max(root.val, maxi))
    def goodNodes(self, root: TreeNode) -> int:
        return self.recur(root, -10**5)
