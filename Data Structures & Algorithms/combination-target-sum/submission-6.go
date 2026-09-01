func combinationSum(nums []int, target int) [][]int {
    sol := []int {} 
	res := [][]int {}

	var backtrack func(i int, summ int) 

	backtrack = func(i int, summ int) {
		if summ == target {
			res = append(res, append([]int{}, sol...))
			return 
		}

		for j := i; j < len(nums); j++ {
            if summ + nums[j] > target {
                continue
            }
            
			sol = append(sol, nums[j])
			backtrack(j, summ + nums[j])
			sol = sol[:len(sol) - 1]
		}
	}

	backtrack(0, 0)
	return res
}
