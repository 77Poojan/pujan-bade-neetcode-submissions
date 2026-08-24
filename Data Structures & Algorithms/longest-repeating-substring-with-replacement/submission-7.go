func characterReplacement(s string, k int) int {
    dp := make([]int, 26)
    l := 0
    maxx := 0
    res := 0

    for r, ch := range(s) {
        dp[ch - 'A'] += 1
        w := r - l + 1
        maxx = max(maxx, dp[ch - 'A'])

        for w - maxx > k {
            dp[s[l] - 'A'] -= 1
            l += 1
            w = r - l + 1
        }
        res = max(res, w)
    }

    return res
}
