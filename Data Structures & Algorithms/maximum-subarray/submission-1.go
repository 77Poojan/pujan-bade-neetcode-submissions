func maxSubArray(nums []int) int {
    currSum := nums[0]
	maxSum := nums[0]

	for _, num := range nums[1:] {
		currSum = max(num, currSum + num)
		maxSum = max(maxSum, currSum)
	}
	
	return maxSum
}
