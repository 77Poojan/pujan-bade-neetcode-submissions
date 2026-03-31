class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = [0] * 26
        y = [0] * 26
        n1 = len(s1)
        n2 = len(s2)


        if n1 > n2:
            return False

        for i in range(n1):
            x[ord(s1[i]) - ord("a")] += 1
            y[ord(s2[i]) - ord("a")] += 1

        if x == y:
            return True

        for k in range(n1, n2):
            y[ord(s2[k]) - ord("a")] += 1
            y[ord(s2[k-n1]) - ord("a")] -= 1
            if x == y:
                return True

        return False