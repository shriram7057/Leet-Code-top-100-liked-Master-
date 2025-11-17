class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        
        def backtrack(i, total, path):
            if total == target:
                res.append(list(path))
                return
            if i >= len(candidates) or total > target:
                return
            path.append(candidates[i])
            backtrack(i, total + candidates[i], path)
            path.pop()
            backtrack(i + 1, total, path)
        
        backtrack(0, 0, [])
        return res
