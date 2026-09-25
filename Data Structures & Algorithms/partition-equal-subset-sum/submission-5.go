func canPartition(nums []int) bool {
    total := sumOf(nums)
    if total % 2 != 0 {
        return false
    }

    target := total / 2
    dp := make([]bool, target + 1)
    dp[0] = true

    for _, num := range nums {
        for j := target; j >= num; j-- {
            dp[j] = dp[j] || dp[j-num]
        }
    }

    return dp[target]
}

func sumOf(nums []int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}