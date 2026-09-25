func combinationSum4(nums []int, target int) int {
    dp := map[int]int{0: 1}

    for j := 1; j <= target; j++ {
        dp[j] = 0
        for _, num := range nums {
            dp[j] += dp[j-num]
        }
    }

    return dp[target]
}