class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev1, prev2, curr = 0, 1, 1

        for i in range(3, n+1):
            prev1, prev2, curr = prev2, curr, prev1 + prev2 + curr 
        
        return curr