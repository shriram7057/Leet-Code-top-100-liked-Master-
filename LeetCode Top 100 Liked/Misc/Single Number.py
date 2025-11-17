class Solution(object):
    def singleNumber(self, nums):
        x = 0
        for n in nums:
            x ^= n
        return x
