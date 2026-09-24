func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    for i := 1; i <= amount; i++ {
        dp[i] = amount + 1 
    }
    // dp[0] = 0 already, by default

    for a := 1; a <= amount; a++ {
        for c := 0; c < len(coins); c++ {
            if coins[c] <= a {
                dp[a] = min(dp[a], 1 + dp[a - coins[c]])
            }
        }
    }

    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
}