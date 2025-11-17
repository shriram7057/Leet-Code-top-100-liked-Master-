class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        max_len = 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            cur_len = max(len1, len2)
            if cur_len > max_len:
                max_len = cur_len
                start = i - (cur_len - 1) // 2

        return s[start:start + max_len]
