class Solution(object):
    def pathSum(self, root, targetSum):
        self.count = 0
        prefix = {0: 1}
        
        def dfs(node, curr):
            if not node:
                return
            curr += node.val
            self.count += prefix.get(curr - targetSum, 0)
            prefix[curr] = prefix.get(curr, 0) + 1
            
            dfs(node.left, curr)
            dfs(node.right, curr)
            
            prefix[curr] -= 1
        
        dfs(root, 0)
        return self.count
