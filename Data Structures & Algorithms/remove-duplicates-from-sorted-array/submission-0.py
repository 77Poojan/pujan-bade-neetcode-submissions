class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 1
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            
            else:
                i += 1 
                nums[i] = nums[j]   
                j += 1
                k += 1
                
        return len(nums[:k])
        