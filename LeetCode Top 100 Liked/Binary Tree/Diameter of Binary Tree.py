class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.ans = max(self.ans, l + r)
            return 1 + max(l, r)
        
        depth(root)
        return self.ans
