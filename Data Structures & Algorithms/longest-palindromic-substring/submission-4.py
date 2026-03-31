class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # odd length
            s1 = expand(i, i)
            # even length
            s2 = expand(i, i+1)

            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2

        return res