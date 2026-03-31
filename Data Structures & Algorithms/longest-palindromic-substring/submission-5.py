class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def extract_palindrome(l , r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]


        for i in range(len(s)):
            n1 = extract_palindrome(i, i)
            n2 = extract_palindrome(i, i + 1)
            if len(res) < len(n1):
                res = n1

            if len(res) < len(n2):
                res = n2

        return res
                
