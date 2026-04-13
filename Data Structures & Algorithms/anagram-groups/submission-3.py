class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     groups[key].append(s)
        
        # return list(groups.values())  


        groups = defaultdict(list)
        res = []

        for s in strs:
            words = [0] * 26
            for ch in s:
                words[ord(ch) - ord("a")] += 1
            groups[tuple(words)].append(s)

        return [g for g in groups.values()]  