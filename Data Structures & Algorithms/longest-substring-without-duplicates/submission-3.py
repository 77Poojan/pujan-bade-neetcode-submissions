class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        maxSub = 0
        i, n = 0, len(s)
        j = 0

        while i < n:
            while j < n and s[i] in subString:
                subString.remove(s[j])
                j += 1

            maxSub = max(maxSub, (i - j) + 1)
            subString.add(s[i])
            i += 1
        
        return maxSub