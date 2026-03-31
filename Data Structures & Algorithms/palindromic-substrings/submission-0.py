class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        l = []

        def expand(i, j):
            res = 0
            while i >= 0 and j < n and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res

        for i in range(n):
            res += expand(i, i)
            res += expand(i, i + 1)
        return res