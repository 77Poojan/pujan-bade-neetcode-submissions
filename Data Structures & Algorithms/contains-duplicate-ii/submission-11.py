class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, len(nums) - 1

        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                j += 1
        
        return False