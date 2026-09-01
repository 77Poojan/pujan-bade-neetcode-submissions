func combinationSum2(candidates []int, target int) [][]int {
    sort.Ints(candidates)

 	sol := []int {} 
	res := [][]int {}

	var backtrack func(i int, summ int) 

	backtrack = func(i int, summ int) {
		if summ == target {
			res = append(res, append([]int{}, sol...))
			return 
		}

		for j := i; j < len(candidates); j++ {
            if j > i && candidates[j] == candidates[j - 1] {
                continue
            }
            if summ + candidates[j] > target  {
                break
            }

			sol = append(sol, candidates[j])
			backtrack(j + 1, summ + candidates[j])
			sol = sol[:len(sol) - 1]
		}
	}

	backtrack(0, 0)
	return res
}
