class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        ch1 = [0] * 26
        ch2 = [0] * 26

        for i in range(n1):
            ch1[ord(s1[i]) - 97] += 1
            ch2[ord(s2[i]) - 97] += 1
        
        if ch1 == ch2:
            return True
        
        for j in range(n1, n2):
            ch2[ord(s2[j]) - 97] += 1
            ch2[ord(s2[j - n1]) - 97] -= 1
            if ch1 == ch2:
                return True
        
        return False