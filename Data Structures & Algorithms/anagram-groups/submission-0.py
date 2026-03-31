class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        groups = [[strs[0]]]
        for s in strs[1:]:
            added = False
            for idx, group in enumerate(groups):
                if Counter(group[0]) == Counter(s):
                    groups[idx].append(s)
                    added = True
                    break
            if not added:
                groups.append([s])            
        return groups   