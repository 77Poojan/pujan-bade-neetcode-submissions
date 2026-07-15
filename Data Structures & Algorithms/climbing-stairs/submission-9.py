class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        prev, curr = 0, 1

        for _ in range(n):
            prev, curr = curr, prev + curr

        return curr

        

