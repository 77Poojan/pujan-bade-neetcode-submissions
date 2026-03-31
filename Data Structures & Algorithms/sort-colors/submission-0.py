class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for num in nums:
            arr[num] +=1
            

        j = 0
        for i in range(len(arr)):
            count = arr[i]
            while count > 0:
                nums[j] = i
                count -= 1
                j += 1
                
        return nums
        
    