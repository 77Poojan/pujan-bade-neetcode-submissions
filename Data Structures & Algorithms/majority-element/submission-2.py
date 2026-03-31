class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev = nums[0]
        count = 1

        for n in nums[1:]:
            if count == 0:
                prev = n
        
            if prev == n:
                count += 1
            else:
                count -= 1

        return prev
            
            