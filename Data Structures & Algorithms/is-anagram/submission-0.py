class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        
        if len(c1) != len(c2):
                return False
        
        for k, v in c1.items():
                if k not in c2.keys() or v != c2[k]: 
                    return False 
                    
        return True