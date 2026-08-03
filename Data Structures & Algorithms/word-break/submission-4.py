class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1 , -1):
            for w in word_set:
                if s[i : i + len(w)] == w and dp[i + len(w)]:
                    dp[i] = True
                    break

        return dp[0]