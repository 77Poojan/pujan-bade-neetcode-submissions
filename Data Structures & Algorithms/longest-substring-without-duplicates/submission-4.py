class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        traced = set()
        l = 0
        maxx = 0

        for r in range(len(s)):
            while s[r] in traced:
                traced.remove(s[l])
                l += 1

            traced.add(s[r])
            maxx = max(maxx, r - l + 1)

        return maxx

            


