class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        ch = set()
        maxx = float("-inf")

        while r < n:
            while s[r] in ch:
                ch.remove(s[l])
                l += 1
            maxx = max(maxx, r - l + 1)
            ch.add(s[r])
            r += 1
            
        return 0 if maxx == float("-inf") else maxx