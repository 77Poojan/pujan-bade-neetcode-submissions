func mySqrt(x int) int {
    if x == 0 {
        return 0
    }

    left := 1
    right := x

    for left <= right {
        mid := left + (right-left)/2

        if mid * mid == x {
            return mid
        } else if mid * mid > x {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return right
}
