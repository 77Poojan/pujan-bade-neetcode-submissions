from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s) - 1
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)

            for j in range(start, min(i + maxJump + 1, n + 1)):
                if s[j] == "0":
                    if j == n:
                        return True
                    q.append(j)
                
            farthest = i + maxJump
        
        return False


            
                
                

