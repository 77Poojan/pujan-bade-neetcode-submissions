class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return nums[0]
        if n == 1:
            return nums[1]
        else:
            prev, curr = 0, 0

            for i in range(2, n+1):
                prev, curr = curr, min(prev + cost[i-2], curr + cost[i-1])
            return curr