class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSum = 0
        hashMap = {0: 1}
        count = 0

        for i in range(len(nums)):
            totalSum += nums[i]
            temp = totalSum - k

            count += hashMap.get(temp, 0)
            hashMap[totalSum] = 1 + hashMap.get(totalSum, 0)
        
        return count


