func permuteUnique(nums []int) [][]int {
	count := make(map[int]int)
	for _, n := range nums {
		count[n]++
	}

	sol := []int {} 
	res := [][]int {}
	var backtrack func() 

	backtrack = func() {
		if len(sol) == len(nums) {
			res = append(res, append([]int{}, sol...))
		}

		for val, c := range count {
            if c == 0 {
				continue
			}

			count[val]--
			sol = append(sol, val)
			backtrack()

			sol = sol[:len(sol) - 1]
			count[val]++
		}
	}

	backtrack()
	return res
}
