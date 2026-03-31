class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = s[0]
        summ = 0
        for ch in s[1:]:
            summ += abs(ord(prev) - ord(ch))
            prev = ch
        return summ