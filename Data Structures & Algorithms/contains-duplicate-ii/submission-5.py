class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        n = len(nums)
        j = 0

        for i in range(n):
            if abs(i - j) > k:
                windows.remove(nums[j])
                j += 1
            if nums[i] in windows:
                return True
            windows.add(nums[i])
        return False