func subsetXORSum(nums []int) int {
	summ := 0
	var backtrack func(i int, currSum int)

	backtrack = func(i int, currSum int) {
		if i == len(nums) {
			summ += currSum
            return
		}

		backtrack(i + 1, currSum)
		backtrack(i + 1, nums[i] ^ currSum)
	}

	backtrack(0, 0)
	return summ
}
