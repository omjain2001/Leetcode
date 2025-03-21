# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def recur(node):
            if node:
                result.append(str(node.val))
                recur(node.left)
                recur(node.right)
            else:
                result.append("#")
        
        result = []
        recur(root)
        return ' '.join(result)
        

    def deserialize(self, data):
        print(data)
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def recur():
            val = next(data)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = recur()
            node.right = recur()
            return node
        
        data = iter(data.split())
        return recur()

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))