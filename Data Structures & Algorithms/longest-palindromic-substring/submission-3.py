class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def expand(i, j):
            while i >= 0 and j < n  and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1 : j]

        for i in range(n):
            p1 = expand(i, i)
            p2 = expand(i, i+1)
            
            if len(p1) > len(res):
                res = p1

            if len(p2) > len(res):
                res = p2

        return res