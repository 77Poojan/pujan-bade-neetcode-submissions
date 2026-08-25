func findClosestElements(arr []int, k int, x int) []int {
    l := 0
    r := len(arr) - 1
    w := r - l + 1

    for w > k {
        a := arr[l]
        b := arr[r]
        if abs(a-x) > abs(b-x) {
            l++
        } else {
            r--
        }
        w = r - l + 1
    }

    return arr[l : r+1]
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}
