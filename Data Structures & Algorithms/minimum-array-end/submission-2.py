class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        for i in range(64):
            if not (x >> i) & 1:
                x |= (n & 1) << i
                n >>= 1
        return x
