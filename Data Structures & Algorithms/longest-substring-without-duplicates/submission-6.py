class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        traced = set()
        i, j = 0, 0
        n = len(s)
        maxx =0

        while j < n:
            while i < n and s[j] in traced:
                traced.remove(s[i])
                i += 1
            maxx = max(maxx, j - i + 1)
            traced.add(s[j])
            j += 1
        
        return maxx


