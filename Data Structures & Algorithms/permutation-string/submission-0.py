from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        j = 0
        while j < len(s2):
            word = s2[j:j+k]
            if Counter(word) == Counter(s1):
                return True
            j += 1
        return False
    