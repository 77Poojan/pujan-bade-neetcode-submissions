class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch = [0] * 26
        maxx = float("-inf")
        l = 0

        for r in range(len(s)):
            W = r - l + 1
            ch[ord(s[r]) - 65] += 1

            while W - max(ch) > k:
                ch[ord(s[l]) - 65] -= 1
                l += 1
                W = r - l + 1
            
            maxx = max(maxx, W)

        return 0 if maxx == float("-inf") else maxx