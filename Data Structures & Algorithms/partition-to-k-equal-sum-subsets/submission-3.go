func canPartitionKSubsets(nums []int, k int) bool {
    sum := 0
    
    for _, number := range nums {
        sum += number
    }

	if sum % k != 0 {
		return false
	}

	target := sum / k
    sides := make([]int, k)

	if nums[0] > target {
        return false 
    }

    sort.Sort(sort.Reverse(sort.IntSlice(nums)))

	var backtrack func(i int) bool
	backtrack = func(i int) bool {
        if i == len(nums) {
            return true
        }

        for j := 0; j < k; j++ {
            if sides[j] + nums[i] > target {
                continue
            }

            sides[j] +=  nums[i]

            if backtrack(i + 1) {
                return true
            }

            sides[j] -=  nums[i]

            if sides[j] == 0 {
                break
            }
        }

		return false
	}

	return backtrack(0)
}
