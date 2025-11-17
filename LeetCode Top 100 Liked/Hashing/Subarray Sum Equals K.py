class Solution(object):
    def subarraySum(self, nums, k):
        mp = {0: 1}
        s = 0
        count = 0
        
        for n in nums:
            s += n
            count += mp.get(s - k, 0)
            mp[s] = mp.get(s, 0) + 1
        
        return count
