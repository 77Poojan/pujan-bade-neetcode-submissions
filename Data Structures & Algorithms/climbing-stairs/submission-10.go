func climbStairs(n int) int {
    if n == 0 || n == 1{
        return n
    }

    prev := 0
    curr := 1

    for i := 0; i < n; i++ {
        prev, curr = curr, prev + curr
    }

    return curr
}
