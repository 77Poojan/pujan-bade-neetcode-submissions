class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for r in range(len(nums)):
            l = r + 1
            while l < n:
                if nums[l] == nums[r] and abs(r - l) <= k:
                    return True
                l += 1
            
        return False



            

