func combine(n int, k int) [][]int {
 	sol := []int {} 
	res := [][]int {}

	var backtrack func(i int) 

	backtrack = func(i int) {
		if len(sol) == k {
			res = append(res, append([]int{}, sol...))
			return 
		}

		for j := i; j < n + 1; j++ {
			sol = append(sol, j)
			backtrack(j + 1)
			sol = sol[:len(sol) - 1]
		}
	}

	backtrack(1)
	return res
}
