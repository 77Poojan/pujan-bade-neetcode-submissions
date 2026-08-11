class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = 0

        for i in range(len(nums)):
            if n == 0:
                temp = nums[i]
                n = 1
                
            if nums[i] == temp:
                n += 1

            else:
                n -= 1 

        return temp

    
