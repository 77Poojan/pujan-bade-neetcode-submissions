class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     groups[key].append(s)
        
        # return list(groups.values())  
        groups = defaultdict(list)
        for s in strs:
            dp = [0] * 26
            for ch in s:
                dp[ord(ch) - ord("a")] += 1
            groups[tuple(dp)].append(s)
        return list(groups.values())  