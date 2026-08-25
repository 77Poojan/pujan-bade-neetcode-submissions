func maxSlidingWindow(nums []int, k int) []int {
    q := []int{}
    res := []int{}

    for r := range nums {
        for len(q) > 0 && nums[q[len(q)-1]] < nums[r] {
            q = q[:len(q)-1]
        }

        q = append(q, r)

        if q[0] <= r-k {
            q = q[1:]
        }

        if r >= k-1 {
            res = append(res, nums[q[0]])
        }
    }

    return res
}