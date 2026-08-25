class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        l = 0
        best_l = 0
        best_len = float("inf")
        missing = len(t)

        for r, ch in enumerate(s):
            if need.get(ch, 0) > 0:
                missing -= 1
            need[ch] = need.get(ch, 0) - 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_ch = s[l]
                need[left_ch] = need.get(left_ch, 0) + 1

                if need.get(left_ch, 0) > 0:
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]