class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # s = {i: 0 for i in range(1, n+1)}
        
        # for t in trust:
        #     p1, p2 = t
        #     if p1 != p2 and p1 in s:
        #         del s[p1]
        #     if p2 in s:
        #         s[p2] += 1

        # for k in s.keys():
        #     if s[k] == n-1:
        #         return k

        # return -1

        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1

        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1
            
        
        
        
