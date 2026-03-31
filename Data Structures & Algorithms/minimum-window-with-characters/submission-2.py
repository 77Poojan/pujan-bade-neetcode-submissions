class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = Counter(t)
        have, need = 0, len(target)
        window = {}

        res, minLen = [-1, -1], float("inf")
        l = 0

        for r in range(n):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0) 

            if ch in target and window[ch] == target[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    res = [l, r] 
                    minLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        l, r = res   
        return s[l:r+1] if res != float("inf") else ""