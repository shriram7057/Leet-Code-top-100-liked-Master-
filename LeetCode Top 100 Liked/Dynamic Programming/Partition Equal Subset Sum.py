class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = set([0])
        for n in nums:
            new_dp = set(dp)
            for t in dp:
                if t + n == target:
                    return True
                if t + n < target:
                    new_dp.add(t + n)
            dp = new_dp
        return target in dp
