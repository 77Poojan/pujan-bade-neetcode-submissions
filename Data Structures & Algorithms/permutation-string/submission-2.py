class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = [0] * 26
        y = [0] * 26
        
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        for i in range(k):
            x[ord(s1[i]) - ord("a")] += 1
            y[ord(s2[i]) - ord("a")] += 1
        
        if x == y:
            return True
        
        for j in range(k, n):
            y[ord(s2[j]) - ord("a")] += 1
            y[ord(s2[j - k]) - ord("a")] -= 1
            if x == y:
                return True

        return False
