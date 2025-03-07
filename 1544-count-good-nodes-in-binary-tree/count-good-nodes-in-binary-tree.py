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
        # return self.recur(root, -10**5)
        if root == None: return 0
        q = [(root, root.val)]
        count = 0
        while(len(q) > 0):
            node, val = q[0]
            q.pop(0)
            if node.val >= val: count += 1
            if node.left: q.append((node.left, max(node.val, val)))
            if node.right: q.append((node.right, max(node.val, val)))
        return count
