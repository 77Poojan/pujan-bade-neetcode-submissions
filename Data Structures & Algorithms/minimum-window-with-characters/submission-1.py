class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = Counter(t)
        minn = None

        for r in range(n):
            window = Counter()
            subb = ""

            for l in range(r, n):
                subb += s[l]
                window[s[l]] += 1

                # Check if window satisfies target
                if all(window[c] >= target[c] for c in target):
                    if minn is None or len(subb) < len(minn):
                        minn = subb
                    break   # stop expanding this window

        return minn if minn else ""