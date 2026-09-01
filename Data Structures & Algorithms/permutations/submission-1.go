func permute(nums []int) [][]int {
	sol := []int {} 
	res := [][]int {}
	used := make([]bool, len(nums))

	var backtrack func(i int) 

	backtrack = func(i int) {
		if i == len(nums) {
			res = append(res, append([]int{}, sol...))
			return 
		}

		for j := 0; j < len(nums); j++ {
            if used[j] {
				continue
			}
			
			used[j] = true
			sol = append(sol, nums[j])
			backtrack(i + 1)
			sol = sol[:len(sol) - 1]
			used[j] = false
		}
	}

	backtrack(0)
	return res
}
