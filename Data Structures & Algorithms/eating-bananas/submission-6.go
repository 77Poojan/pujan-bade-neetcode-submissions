import "slices"

func rate(r int, piles []int) int {
    count := 0
    for _, pile := range piles {
        count += (pile + r - 1) /r
    }
    return count
}

func minEatingSpeed(piles []int, h int) int {
    left := 1
    right := slices.Max(piles)
    res := right

    for left <= right {
        mid := left + (right - left) / 2

        if rate(mid, piles) <= h {
            res = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return res 	
}