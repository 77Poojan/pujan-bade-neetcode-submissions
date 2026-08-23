class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dp = [0] * 26
        l, res = 0, 0
        maxx =0

        for r in range(len(s)):
            ch = ord(s[r]) - ord("A")
            dp[ch] += 1
            maxx = max(maxx, dp[ch])
            w = r - l + 1

            while w - maxx > k:
                dp[ord(s[l]) - ord("A")] -= 1
                l += 1
                w = r - l + 1

            res = max(res, w)

        return res