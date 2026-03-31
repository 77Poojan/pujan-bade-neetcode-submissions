class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        prev, curr = 0, 0

        for i in range(2, len(cost)+1):
            prev, curr = curr, min(curr + cost[i-1], prev + cost[i-2])
        
        return curr
