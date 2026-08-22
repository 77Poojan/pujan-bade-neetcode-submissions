func splitArray(nums []int, k int) int {
    canSplit := func(largest int) bool {
        subarray := 1
        curSum := 0
        for _, num := range nums {
            curSum += num
            if curSum > largest {
                subarray++
                if subarray > k {
                    return false
                }
                curSum = num
            }
        }
        return true
    }

    l, r := 0, 0
    for _, num := range nums {
        if num > l {
            l = num
        }
        r += num
    }
    res := r

    for l <= r {
        mid := l + (r-l)/2
        if canSplit(mid) {
            res = mid
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return res
}