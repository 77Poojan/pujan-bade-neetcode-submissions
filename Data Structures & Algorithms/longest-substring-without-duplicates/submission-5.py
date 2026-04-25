class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        traced = set()
        l, r = 0, 0
        maxx = 0
        n = len(s)

        while r < n:
            while l < n and s[r] in traced:
                traced.remove(s[l])
                l += 1
            maxx = max(maxx, r - l + 1)
            traced.add(s[r])
            r += 1
        
        return maxx



            


