func minSubArrayLen(target int, nums []int) int {
	l := 0
	total := 0
	w := math.MaxInt32

	for r, num := range(nums) {
        total += num
		for total >= target {
            w = min(w, r - l + 1)
			total -= nums[l]
			l += 1
		}
	}

	if w == math.MaxInt32 {
		return 0
	}

	return w
}
