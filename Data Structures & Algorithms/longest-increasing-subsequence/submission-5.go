func lengthOfLIS(nums []int) int {
    n := len(nums)
    dp := make([]int, n)
    
    for i := range dp {
        dp[i] = 1
    }

    for i := 0; i < n; i++ {
        for j := 0; j < i; j++ {
            if nums[j] < nums[i] {
                dp[i] = max(dp[i], 1+dp[j])
            }
        }
    }

    ans := 0
    for _, v := range dp {
        ans = max(ans, v)
    }
    return ans
}