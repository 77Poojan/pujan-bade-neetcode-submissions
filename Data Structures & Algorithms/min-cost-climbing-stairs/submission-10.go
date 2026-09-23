func minCostClimbingStairs(cost []int) int {
	n := len(cost)
    prev := cost[0]
    curr := cost[1]

    for i := 2; i < n; i++ {
        prev, curr = curr, cost[i] + min(curr, prev)
    }

    return min(prev, curr)
}
