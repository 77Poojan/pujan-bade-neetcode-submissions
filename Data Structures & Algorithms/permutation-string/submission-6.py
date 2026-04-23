class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dp1 = [0] * 26
        dp2 = [0] * 26

        for i in range(len(s1)):
            dp1[ord(s1[i]) - 97] += 1
            dp2[ord(s2[i]) - 97] += 1

        if dp1 == dp2:
            return True

        for j in range(len(s1), len(s2)):
            dp2[ord(s2[j]) - 97] += 1
            dp2[ord(s2[j - len(s1)]) - 97] -= 1

            if dp1 == dp2:
                return True

        return False