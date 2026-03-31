class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] in s or nums[j] in s or nums[i] == nums[j]:
                return True
            else:
                s.add(nums[i])
                s.add(nums[j])
            i += 1
            j -= 1
        return False