class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = {}

        def insert(word):
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["#"] = True

        for d in dictionary:
            insert(d)

        n = len(s)
        dp = [0] * (n+1)
        

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            t = trie 
            for j in range(i, n):
                w = s[j]
                if w not in t:
                    break

                t = t[w]
                if "#" in t:
                    dp[i] = min(dp[i], dp[j+1])
        
        return dp[0]