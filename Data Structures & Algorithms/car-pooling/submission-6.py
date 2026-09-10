class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = float("inf")
        end = float("-inf")

        for _, s, e in trips:
            start = min(start, s)
            end = max(end, e)

        dp = [0] * (end + 1)

        for p, s, e in trips:
            dp[s] += p
            dp[e] -= p

        curr = 0
        for i in range(len(dp)):
            curr += dp[i]
            if curr > capacity:
                return False

        return True