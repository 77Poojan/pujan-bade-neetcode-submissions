class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        maxx = float("-inf")
        l = 0
        for r in range(len(s)):
            while s[r] in word:
                word.remove(s[l])
                l += 1
            maxx = max(maxx, r - l + 1)
            word.add(s[r])
        return 0 if maxx == float("-inf") else maxx