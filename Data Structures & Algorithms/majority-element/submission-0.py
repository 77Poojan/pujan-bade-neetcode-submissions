class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if prev == nums[i]:
                count += 1
            else:
                count -= 1
                
            if count < 0:
                prev = nums[i]
                count = 0
        return prev
            
