class Solution(object):
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    backtrack(path + [nums[i]])
                    used[i] = False

        backtrack([])
        return res
