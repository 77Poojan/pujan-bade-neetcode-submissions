class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(n):
            # odd-length palindrome
            p1 = expand(i, i)
            # even-length palindrome
            p2 = expand(i, i + 1)

            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res