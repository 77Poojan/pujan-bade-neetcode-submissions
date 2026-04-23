class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dp = [0] * 26
        maxx = 0
        res = 0

        for r in range(len(s)):
            ch = ord(s[r]) - ord("A")
            dp[ch] += 1
            maxx = max(maxx, dp[ch])
 

            while r - l + 1 - maxx > k:
                dp[ord(s[l]) - ord("A")] -= 1
                l += 1
  
            res = max(res, r - l + 1)

        return res



            





