func subsets(nums []int) [][]int {
	sol := []int {} 
	res := [][]int {}

	var backtrack func(i int) 
	backtrack = func(i int) {
		res = append(res, append([]int{}, sol...))

		for j := i; j < len(nums); j++ {
			if j > i && nums[j] == nums[j - 1] {
				continue
			}

			sol = append(sol, nums[j])
			backtrack(j + 1)
			sol = sol[:len(sol) - 1]
		}
	}

	backtrack(0)
	return res
}
