func threeSum(nums []int) [][]int {
    sort.Ints(nums)

    n := len(nums)
    result := [][]int{}

    for i := 0; i < n-2; i++ {

        // Skip duplicate first elements
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }

        j := i + 1
        k := n - 1

        for j < k {
            summ := nums[i] + nums[j] + nums[k]

            if summ == 0 {
                result = append(result, []int{nums[i], nums[j], nums[k]})

                j++
                k--

                // Skip duplicate second elements
                for j < k && nums[j] == nums[j-1] {
                    j++
                }

                // Skip duplicate third elements
                for j < k && nums[k] == nums[k+1] {
                    k--
                }

            } else if summ < 0 {
                j++
            } else {
                k--
            }
        }
    }

    return result
}