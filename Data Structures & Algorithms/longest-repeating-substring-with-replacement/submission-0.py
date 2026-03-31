class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch = [0] * 26
        l = 0
        maxx = 0

        for r in range(len(s)):
            W = r - l + 1
            ch[ord(s[r]) - 65] += 1

            while W - max(ch) > k:
                ch[ord(s[l]) - 65] -= 1
                l += 1
                W = r - l + 1
                
            maxx = max(maxx, W)
        return maxx