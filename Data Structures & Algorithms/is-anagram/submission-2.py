class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # c1 = Counter(s)
        # c2 = Counter(t)
        
        # if len(c1) != len(c2):
        #         return False
        
        # for k, v in c1.items():
        #     if k not in c2.keys() or v != c2[k]: 
        #         return False 
                    
        # return True
        if len(s) != len(t):
            return False

        n = len(s)
        dp = [0] * 26

        for i in range(len(s)):
            dp[ord(s[i]) - 97] += 1
            dp[ord(t[i]) - 97] -= 1

        for val in dp:
            if val != 0:
                return False
        
        return True