# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def recur(io_s, io_e, po_s, po_e):
            if io_s > io_e:
                return None
            
            i = hashmap[preorder[po_s]]
            # while(i <= io_e and inorder[i] != preorder[po_s]):
            #     i += 1
            
            newnode = TreeNode(preorder[po_s])
            newnode.left = recur(io_s, i-1, po_s+1, po_s + i - io_s)
            newnode.right = recur(i+1, io_e, po_s + i - io_s + 1, po_e)
            return newnode
        
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        return recur(0, len(inorder)-1, 0, len(preorder)-1)
            
        