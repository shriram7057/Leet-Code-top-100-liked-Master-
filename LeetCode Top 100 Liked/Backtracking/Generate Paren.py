class Solution(object):
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(openN, closeN, path):
            if openN == closeN == n:
                res.append(path)
                return
            if openN < n:
                backtrack(openN + 1, closeN, path + "(")
            if closeN < openN:
                backtrack(openN, closeN + 1, path + ")")
        
        backtrack(0, 0, "")
        return res
