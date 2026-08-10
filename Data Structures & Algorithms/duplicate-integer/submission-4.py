class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] in s:
                return True

            s.add(nums[i])

            if nums[j] in s:
                return True

            s.add(nums[j])
            
            i += 1
            j -= 1


        return False