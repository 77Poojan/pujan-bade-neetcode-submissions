class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # j = 0
        # n = len(nums)
        # s = []
        
        # while j < n:
        #     if nums[j] != val:
        #         s.append(nums[j]) 
        #     j += 1
        
        # for i in range(len(s)):
        #     nums[i] = s[i]

        # return len(s)

        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n 

