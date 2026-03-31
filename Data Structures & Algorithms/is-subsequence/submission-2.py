class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        new_s = list(s[::-1])
        for ch in t:
            if new_s and ch == new_s[-1]:
                new_s.pop()
        return True if len(new_s) == 0 else False  