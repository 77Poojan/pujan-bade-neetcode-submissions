class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fw = [1] * n 
        bw = [1] * n 

        for i in range(n):
            j = i + 1
            while j < n:
                fw[i] *= nums[j]
                j += 1
        
        for i in range(n - 1, -1, -1):
            j = i - 1
            while j >= 0:
                bw[i] *= nums[j]
                j -= 1

        for i in range(len(fw)):
            fw[i] *= bw[i] 
        
        return fw
        
        