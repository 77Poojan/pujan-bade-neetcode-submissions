func canJump(nums []int) bool {
	n := len(nums)
	goal := n - 1
	for j := n - 2; j >= 0; j-- {
		if j + nums[j] >= goal {
			goal = j
		} 
	}

	return goal == 0
}
