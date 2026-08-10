from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     groups[key].append(s)
        
        # return list(groups.values())  

        groups = defaultdict(list)

        for i in range(len(strs)):
            ch = [0] * 26

            for s in strs[i]:
                ch[ord(s) - 97] += 1
     
            groups[tuple(ch)].append(strs[i])

        return list(groups.values()) 

