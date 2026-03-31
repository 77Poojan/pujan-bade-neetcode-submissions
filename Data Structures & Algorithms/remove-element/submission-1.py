class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        n = len(nums)
        s = []
        while j < n:
            if nums[j] != val:
                s.append(nums[j]) 
            j += 1
        
        for i in range(len(s)):
            nums[i] = s[i]

        return len(s)