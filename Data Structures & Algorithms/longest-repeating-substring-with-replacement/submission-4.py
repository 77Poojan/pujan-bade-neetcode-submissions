class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        subs = [0] * 26
        l = 0
        maxx = 0

        for r in range(len(s)):
            ch = s[r]
            subs[ord(ch) - 65] += 1
            W = r - l + 1 

            while W - max(subs) > k:
                subs[ord(s[l]) - 65] -= 1
                l += 1
                W = r - l + 1 
            maxx = max(maxx, W)
        
        return maxx

